########################################################################################################################
## Mabrains Company LLC
##
## Mabrains Via Generator for Skywaters 130nm
########################################################################################################################
import pya
import math

"""
Mabrains Via Generator for Skywaters 130nm
"""


class ViaGenerator(pya.PCellDeclarationHelper):
    """
    Mabrains Via Generator for Skywaters 130nm
    """

    def __init__(self):
        ## Initialize super class.
        super(ViaGenerator, self).__init__()

        # declare the parameters
        self.param("ls", self.TypeLayer, "Starting Layer", default=pya.LayerInfo(1, 0))
        self.param("le", self.TypeLayer, "Ending Layer", default=pya.LayerInfo(1, 0))
        self.param("w", self.TypeDouble, "Width", default=1.5)
        self.param("l", self.TypeDouble, "Length", default=5.0)

        # Below shows how to create hidden parameter is used to determine whether the radius has changed
        # or the "s" handle has been moved
        ## self.param("ru", self.TypeDouble, "Radius", default = 0.0, hidden = True)
        ## self.param("rd", self.TypeDouble, "Double radius", readonly = True)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "Via(LS=" + str(self.ls) + ",LE=" + str(self.le) + ")"

    def coerce_parameters_impl(self):

        # We employ coerce_parameters_impl to decide whether the handle or the
        # numeric parameter has changed (by comparing against the effective
        # radius ru) and set ru to the effective radius. We also update the
        # numerical value or the shape, depending on which on has not changed.
        pass

    def can_create_from_shape_impl(self):
        # Implement the "Create PCell from shape" protocol: we can use any shape which
        # has a finite bounding box
        return self.shape.is_box() or self.shape.is_polygon() or self.shape.is_path()

    def parameters_from_shape_impl(self):
        # Implement the "Create PCell from shape" protocol: we set r and l from the shape's
        # bounding box width and layer
        self.w = self.shape.bbox().width() * self.layout.dbu
        self.l = self.shape.bbox().length() * self.layout.dbu
        self.ls = self.layout.get_info(self.layer)

    def transformation_from_shape_impl(self):
        # Implement the "Create PCell from shape" protocol: we use the center of the shape's
        # bounding box to determine the transformation
        return pya.Trans(self.shape.bbox().p1())

    def produce_impl(self):
        ru_dbu = self.w / self.layout.dbu

        # compute the circle
        pts = []
        da = math.pi * 2 / 4
        for i in range(0, 4):
            pts.append(pya.Point.from_dpoint(pya.DPoint(ru_dbu * math.cos(i * da), ru_dbu * math.sin(i * da))))

        # create the shape
        self.cell.shapes(self.ls_layer).insert(pya.Polygon(pts))
