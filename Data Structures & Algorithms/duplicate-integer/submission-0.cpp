class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> tracked;
        for(int i = 0; i < nums.size(); i++){
            if(tracked.count(nums[i])) 
                return true;

            tracked.insert(nums[i]);
            std::cout << nums[i] << " ";
        }
        return false;
    }
};