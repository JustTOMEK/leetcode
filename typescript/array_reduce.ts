type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    let number_to_return : number = init;

    for (let i: number = 0; i < nums.length; i ++)
    {
        number_to_return = fn(number_to_return, nums[i]);
    }

    return number_to_return;
}

const numerrs : number[] = [1, 2, 3, 4];
function dodawanie(accum: number, curr: number) { return accum + curr; }

reduce(numerrs, dodawanie, 10);