class Solution(object):
    def maximalRectangle(self, matrix):

        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    @staticmethod
    def largestRectangleArea(heights):
        stack = []
        max_area = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area
