function twoSum(nums: number[], target: number): number[] {

    const dictionary : {[key: number] : number} = {};

    for (let i : number = 0; i < nums.length; i ++)
    {
        dictionary[nums[i]] = i;
    }

    for (let i : number = 0; i < nums.length; i ++)
    {
        if ((target - nums[i]) in dictionary && dictionary[target - nums[i]] != i)
        {
            return [i, dictionary[target - nums[i]]];
        }
    }
}