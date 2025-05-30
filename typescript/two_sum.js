function twoSum(nums, target) {
    var dictionary = {};
    for (var i = 0; i < nums.length; i++) {
        dictionary[nums[i]] = i;
    }
    for (var i = 0; i < nums.length; i++) {
        if ((target - nums[i]) in dictionary && dictionary[target - nums[i]] != i) {
            return [i, dictionary[target - nums[i]]];
        }
    }
}
