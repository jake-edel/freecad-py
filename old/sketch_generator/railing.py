from old.sketch_generator.triangle_helper import TriangleHelper
from old.sketch_generator.bottom_post import BottomPost
from top_rail import TopRail
from top_post import TopPost


class Railing:

    def __init__(self, rise, run):
        self.postHeight = 36
        self.materialWidth = 1.5
        self.rise = rise
        self.run = run
        self.railAngle = TriangleHelper.rail_angle(rise, run)
        self.mitreAngle = TriangleHelper.mitre_angle(self.railAngle)
        self.partsList = self.generate_parts()

    def generate_parts(self):
        botPost = BottomPost(self.materialWidth, self.postHeight, self.mitreAngle, self.railAngle)
        topRail = TopRail(self.materialWidth, self.rise, self.run, self.mitreAngle, self.railAngle, botPost)
        topPost = TopPost(self.materialWidth, self.postHeight, self.rise, self.run, self.mitreAngle, self.railAngle)
        partsList = [botPost, topRail, topPost]
        return partsList

