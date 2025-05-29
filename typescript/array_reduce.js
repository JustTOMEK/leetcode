function reduce(nums, fn, init) {
    var number_to_return = init;
    for (var i = 0; i < nums.length; i++) {
        number_to_return = fn(number_to_return, nums[i]);
    }
    return number_to_return;
}
var numerrs = [1, 2, 3, 4];
function dodawanie(accum, curr) { return accum + curr; }
reduce(numerrs, dodawanie, 10);
