class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while (left != right) :
            h = min(height[left], height[right])
            w = right - left
            current_area = h*w
            
            max_area = max_area if max_area > current_area else current_area
            
            # 높이가 작은 쪽이 이동 - 더 큰 높이 값이 나올 수 있기 때문
            if (height[left] < height[right]):
                left += 1
            else:
                 right -= 1

        return max_area