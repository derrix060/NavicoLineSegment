import unittest
from LineSegment import Point, LineSegment

class TestLineSegment(unittest.TestCase):

    p0 = Point(0, 0)
    p1 = Point(1, 2)
    p2 = Point(3, -2)
    p3 = Point(-3, 0)
    ls1 = LineSegment(p1, p2)
    ls_x_axis = LineSegment(p0, Point(0.1, 0))
    ls_y_axis = LineSegment(p0, Point(0, 0.1))


    def test_correct_line_segment(self):
        LineSegment(self.p2, self.p1)

    def test_parallel_line_segment_y_axis(self):
        p = Point(self.p1.x, self.p1.y + 0.1)
        LineSegment(self.p1, p)

    def test_parallel_line_segment_x_axis(self):
        p = Point(self.p1.x + 0.1, self.p1.y)
        LineSegment(self.p1, p)

    def test_point_as_line_segment(self):
        with self.assertRaises(ValueError):
            LineSegment(self.p1, self.p1)

        with self.assertRaises(ValueError):
            p = Point(self.p1.x, self.p1.y)
            LineSegment(self.p1, p)

    def test_slope(self):
        self.assertEqual(self.ls1.slope, -2)

    def test_slope_none(self):
        p = Point(self.p1.x, self.p1.y + 0.1)
        ls2 = LineSegment(self.p1, p)
        self.assertIsNone(ls2.slope)

    def test_slope_zero(self):
        p = Point(self.p1.x + 0.1, self.p1.y)
        ls2 = LineSegment(self.p1, p)
        self.assertEqual(ls2.slope, 0)

    def test_lengh(self):
        self.assertEqual(int(self.ls1.lengh * self.ls1.lengh), 20)

    def test_lengh_parallel_x_axis(self):
        self.assertEqual(self.ls_x_axis.lengh, 0.1)

    def test_lengh_parallel_y_axis(self):
        self.assertEqual(self.ls_y_axis.lengh, 0.1)

    def test_parallel_same_line(self):
        self.assertTrue(self.ls1.is_parallel(self.ls1))

    def test_parallel_line(self):
        p_1 = Point(self.p1.x -0.1, self.p1.y)
        p_2 = Point(self.p2.x -0.1, self.p2.y)
        ls2 = LineSegment(p_1, p_2)
        self.assertTrue(self.ls1.is_parallel(ls2))
        self.assertTrue(ls2.is_parallel(self.ls1))

    def test_parallel_y_axis(self):
        ls_2 = LineSegment(Point(0.1, 0), Point(0.1, 0.1))
        self.assertTrue(self.ls_y_axis.is_parallel(ls_2))
        self.assertTrue(ls_2.is_parallel(self.ls_y_axis))

    def test_parallel_x_axis(self):
        ls_2 = LineSegment(Point(0, 0.1), Point(0.1, 0.1))
        self.assertTrue(self.ls_x_axis.is_parallel(ls_2))
        self.assertTrue(ls_2.is_parallel(self.ls_x_axis))

    def test_not_parallel_line(self):
        p = Point(self.p2.x, self.p2.y -0.1)
        ls2 = LineSegment(self.p1, p)
        self.assertFalse(self.ls1.is_parallel(ls2))
        self.assertFalse(ls2.is_parallel(self.ls1))

    def test_perpendicular_line(self):
        ls_1 = LineSegment(self.p0, Point(1, 1))
        ls_2 = LineSegment(Point(0, 1), Point(1, 0))
        self.assertTrue(ls_1.is_perpendicular(ls_2))
        self.assertTrue(ls_2.is_perpendicular(ls_1))
        # Another line
        ls_3 = LineSegment(self.p1, self.p3)
        self.assertTrue(ls_3.is_perpendicular(self.ls1))
        self.assertTrue(self.ls1.is_perpendicular(ls_3))

    def test_perpendicular_axis_lines(self):
        self.assertTrue(self.ls_x_axis.is_perpendicular(self.ls_y_axis))
        self.assertTrue(self.ls_y_axis.is_perpendicular(self.ls_x_axis))

    def test_not_perpendicular_line_p3_y_check(self):
        p1 = Point(-3, 1)
        p2 = Point(-3, -1)
        ls1 = LineSegment(self.p1, p1)
        ls2 = LineSegment(self.p1, p2)
        self.assertFalse(self.ls1.is_perpendicular(ls1))
        self.assertFalse(ls1.is_perpendicular(self.ls1))
        self.assertFalse(self.ls1.is_perpendicular(ls2))
        self.assertFalse(ls2.is_perpendicular(self.ls1))

    def test_not_perpendicular_line_p3_x_check(self):
        p1 = Point(-4, 0)
        p2 = Point(-2, 0)
        ls1 = LineSegment(self.p1, p1)
        ls2 = LineSegment(self.p1, p2)
        self.assertFalse(self.ls1.is_perpendicular(ls1))
        self.assertFalse(ls1.is_perpendicular(self.ls1))
        self.assertFalse(self.ls1.is_perpendicular(ls2))
        self.assertFalse(ls2.is_perpendicular(self.ls1))
    
    def test_not_perpendicular_axis_x_line(self):
        p1 = Point(1, 0)
        p2 = Point(-1, 0)
        ls1 = LineSegment(self.p0, p1)
        ls2 = LineSegment(self.p0, p2)
        self.assertFalse(self.ls_x_axis.is_perpendicular(ls1))
        self.assertFalse(ls1.is_perpendicular(self.ls_x_axis))
        self.assertFalse(self.ls_x_axis.is_perpendicular(ls2))
        self.assertFalse(ls2.is_perpendicular(self.ls_x_axis))

    def test_not_perpendicular_axis_y_line(self):
        p1 = Point(0, 1)
        p2 = Point(0, -1)
        ls1 = LineSegment(self.p0, p1)
        ls2 = LineSegment(self.p0, p2)
        self.assertFalse(self.ls_y_axis.is_perpendicular(ls1))
        self.assertFalse(ls1.is_perpendicular(self.ls_y_axis))
        self.assertFalse(self.ls_y_axis.is_perpendicular(ls2))
        self.assertFalse(ls2.is_perpendicular(self.ls_y_axis))


class TestPoint(unittest.TestCase):
    
    def test_valid_point(self):
        Point(1, 1)

    def test_equals_points(self):
        p1 = Point(1, 1)
        p2 = Point(1, 1)

        self.assertTrue(p1 == p1)
        self.assertTrue(p1 == p2)

    def test_not_equals_x_limits(self):
        p = Point(1, 1)
        p1 = Point(1.1, 1)
        p2 = Point(0.9, 1)

        self.assertFalse(p == p1)
        self.assertTrue(p != p1)
        self.assertFalse(p == p2)
        self.assertTrue(p != p2)
    
    def test_not_equals_y_limits(self):
        p = Point(1, 1)
        p1 = Point(1, 1.1)
        p2 = Point(1, 0.9)

        self.assertFalse(p == p1)
        self.assertTrue(p != p1)
        self.assertFalse(p == p2)
        self.assertTrue(p != p2)



if __name__ == '__main__':
    unittest.main()