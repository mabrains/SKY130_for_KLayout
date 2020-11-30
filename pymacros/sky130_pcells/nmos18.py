########################################################################################################################
## Mabrains Company LLC
##
## Mabrains NMOS 1.8V Generator for Skywaters 130nm
########################################################################################################################
import pya
import math


class NMOS18(pya.PCellDeclarationHelper):
    """
    Mabrains Via Generator for Skywaters 130nm
    """

    def __init__(self):
        ## Initialize super class.
        super(NMOS18, self).__init__()

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
        return "NMOS18(L=" + ('%.3f' % self.l) + ",W=" + ('%.3f' % self.w) + ")"

    def coerce_parameters_impl(self):
        # We employ coerce_parameters_impl to decide whether the handle or the
        # numeric parameter has changed (by comparing against the effective
        # radius ru) and set ru to the effective radius. We also update the
        # numerical value or the shape, depending on which on has not changed.
        pass

    # def can_create_from_shape_impl(self):
    #     # Implement the "Create PCell from shape" protocol: we can use any shape which
    #     # has a finite bounding box
    #     return self.shape.is_box() or self.shape.is_polygon() or self.shape.is_path()
    #
    # def parameters_from_shape_impl(self):
    #     # Implement the "Create PCell from shape" protocol: we set r and l from the shape's
    #     # bounding box width and layer
    #     self.r = self.shape.bbox().width() * self.layout.dbu / 2
    #     self.l = self.layout.get_info(self.layer)
    #
    # def transformation_from_shape_impl(self):
    #     # Implement the "Create PCell from shape" protocol: we use the center of the shape's
    #     # bounding box to determine the transformation
    #     return pya.Trans(self.shape.bbox().center())

    def produce_impl(self):
        start = pya.Point(0,0)
        end = pya.Point(5000, 5000)

        # create the shape
        self.cell.shapes(self.ls).insert(pya.Box(start, end))
