# Python class providing simple drawing primitives. It wraps PIL.Image and PIL.Imagedraw
# 2025 Programming for Chemistry @ UniMI

from PIL import Image, ImageDraw, ImageFont

def _adjust_bbox(x0, y0, x1, y1):
    """
    Adjust bounding box coordinates to ensure proper ordering.
    
    Swaps coordinates if x0 > x1 or y0 > y1 to ensure the bounding box
    has the correct top-left to bottom-right orientation.
    
    Args:
        x0 (int): First x-coordinate
        y0 (int): First y-coordinate  
        x1 (int): Second x-coordinate
        y1 (int): Second y-coordinate
        
    Returns:
        tuple: Adjusted coordinates (x0, y0, x1, y1) in proper order
    """
    if x0 > x1:
        x0, x1 = x1, x0
    if y0 > y1:
        y0, y1 = y1, y0

    return x0, y0, x1, y1


class Canvas:
    """
    A 2D drawing canvas built on top of PIL (Pillow) for creating graphics.
    
    The Canvas class provides a simple, chainable API for drawing shapes, text,
    and other graphics elements. All drawing methods return the Canvas instance
    to allow for method chaining.
    
    Attributes:
        image (PIL.Image): The underlying PIL Image object
        draw (PIL.ImageDraw): The PIL ImageDraw object for drawing operations
        pencolor (str): Current pen/outline color for drawing
        fillcolor (str or None): Current fill color for shapes
        penwidth (int): Current line width for drawing
        font (PIL.ImageFont): Current font for text rendering
    """

    def __init__(self, width=500, height=500, color='white'):
        """
        Initialize a new Canvas with specified dimensions and background color.
        
        Args:
            width (int, optional): Canvas width in pixels. Defaults to 500.
            height (int, optional): Canvas height in pixels. Defaults to 500.
            color (str, optional): Background color name or hex code. Defaults to 'white'.
        """
        self.image = Image.new(mode='RGB', size=(width,height), color=color)
        self.draw = ImageDraw.Draw(self.image)
        self.pencolor = 'black'
        self.fillcolor = None
        self.penwidth = 1
        self.font = ImageFont.truetype("Arial", 12)

    def show(self):
        """
        Get the PIL Image object for display or further processing.
        
        Returns:
            PIL.Image: The canvas as a PIL Image object
        """
        return self.image
    
    def tofile(self, filename):
        """
        Save the canvas to an image file.
        
        Args:
            filename (str): Output filename with extension (e.g., "drawing.png")
        """
        self.image.save(filename)

    def get_width(self):
        """
        Get the canvas width.
        
        Returns:
            int: Canvas width in pixels
        """
        return self.image.size[0]
    
    def get_height(self):
        """
        Get the canvas height.
        
        Returns:
            int: Canvas height in pixels
        """
        return self.image.size[1]

    def set_pencolor(self, color):
        """
        Set the pen color for drawing lines and shape outlines.
        
        Args:
            color (str): Color name ('red', 'blue') or hex code ('#FF0000')
            
        Returns:
            Canvas: This Canvas instance for method chaining
        """
        self.pencolor = color
        return self

    def set_penwidth(self, width):
        """
        Set the width/thickness of lines and shape outlines.
        
        Args:
            width (int): Line width in pixels
            
        Returns:
            Canvas: This Canvas instance for method chaining
        """
        self.penwidth = width
        return self

    def set_fillcolor(self, color):
        """
        Set the fill color for shapes.
        
        Args:
            color (str or None): Fill color name/hex code, or None for no fill
            
        Returns:
            Canvas: This Canvas instance for method chaining
        """
        self.fillcolor = color
        return self

    def line(self, x0, y0, x1, y1):
        """
        Draw a line from one point to another.
        
        Args:
            x0 (int): Starting x-coordinate
            y0 (int): Starting y-coordinate
            x1 (int): Ending x-coordinate
            y1 (int): Ending y-coordinate
            
        Returns:
            Canvas: This Canvas instance for method chaining
        """
        self.draw.line(xy=(x0,y0,x1,y1), fill=self.pencolor, width=self.penwidth, joint='curve')
        return self

    def rectangle(self, x0, y0, x1, y1):
        """
        Draw a rectangle with opposite corners at the specified points.
        
        Args:
            x0 (int): First corner x-coordinate
            y0 (int): First corner y-coordinate
            x1 (int): Opposite corner x-coordinate
            y1 (int): Opposite corner y-coordinate
            
        Returns:
            Canvas: This Canvas instance for method chaining
            
        Note:
            Corner order doesn't matter - coordinates are automatically adjusted.
        """
        x0, y0, x1, y1 = _adjust_bbox(x0, y0, x1, y1)
        self.draw.rectangle(xy=(x0,y0,x1,y1), fill=self.fillcolor, width=self.penwidth, outline=self.pencolor)
        return self

    def text(self, x, y, text, center=False):
        """
        Draw text at the specified position.
        
        Args:
            x (int): Text x-coordinate
            y (int): Text y-coordinate
            text (str): Text string to draw
            center (bool, optional): If True, center text at (x,y). 
                                   If False, position at top-left. Defaults to False.
                                   
        Returns:
            Canvas: This Canvas instance for method chaining
        """
        anchor = 'mm' if center else 'lt'
        self.draw.text(xy=(x, y), text=text, font=self.font, fill=self.pencolor, anchor=anchor)
        return self

    def set_font(self, fontname, fontsize, center=False):
        """
        Set the font for text rendering.
        
        Args:
            fontname (str): Font file name or system font name (e.g., "Arial")
            fontsize (int): Font size in points
            center (bool, optional): Unused parameter (kept for compatibility)
            
        Returns:
            Canvas: This Canvas instance for method chaining
        """
        self.font = ImageFont.truetype(fontname, fontsize)
        return self
    
    def circle(self, x, y, r):
        """
        Draw a circle centered at the specified point.
        
        Args:
            x (int): Center x-coordinate
            y (int): Center y-coordinate
            r (int): Radius in pixels
            
        Returns:
            Canvas: This Canvas instance for method chaining
        """
        self.ellipse(x, y, r, r)
        return self
    
    def ellipse(self, x, y, r1, r2):
        """
        Draw an ellipse centered at the specified point.
        
        Args:
            x (int): Center x-coordinate
            y (int): Center y-coordinate
            r1 (int): Horizontal radius
            r2 (int): Vertical radius
            
        Returns:
            Canvas: This Canvas instance for method chaining
        """
        x0, y0 = x-r1, y-r2
        x1, y1 = x+r1, y+r2
        self.draw.ellipse((x0,y0,x1,y1), fill=self.fillcolor, outline=self.pencolor, width=self.penwidth)
        return self

    def point(self, x, y):
        """
        Draw a single pixel point at the specified coordinates.
        
        Args:
            x (int): Point x-coordinate
            y (int): Point y-coordinate
            
        Returns:
            Canvas: This Canvas instance for method chaining
        """
        self.draw.point((x,y), fill=self.pencolor)
        return self
    
    def lines(self, xy):
        """
        Draw connected line segments through multiple points.
        
        Args:
            xy (list): List of coordinate tuples [(x1,y1), (x2,y2), ...]
            
        Returns:
            Canvas: This Canvas instance for method chaining
            
        Example:
            canvas.lines([(100, 100), (200, 150), (300, 100)])
        """
        self.draw.line(xy, fill=self.pencolor, width=self.penwidth)
        return self

    def polygon(self, xy):
        """
        Draw a filled polygon connecting the specified points.
        
        Args:
            xy (list): List of coordinate tuples defining polygon vertices
            
        Returns:
            Canvas: This Canvas instance for method chaining
            
        Example:
            triangle = [(100, 100), (200, 100), (150, 50)]
            canvas.polygon(triangle)
        """
        self.draw.polygon(xy, fill=self.fillcolor, outline=self.pencolor, width=self.penwidth)
        return self
    
    def fill(self, x, y):
        """
        Flood fill an area starting from the specified point.
        
        Fills a connected area of the same color with the current fill color,
        similar to the "paint bucket" tool in image editors.
        
        Args:
            x (int): Starting x-coordinate for flood fill
            y (int): Starting y-coordinate for flood fill
            
        Returns:
            Canvas: This Canvas instance for method chaining
        """
        ImageDraw.floodfill(self.image, (x,y), value=self.fillcolor)
        return self
