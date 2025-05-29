type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
    let filtered_arr : number[] = [];
    for (let i : number = 0; i < arr.length; i++)
    {
        if (fn(arr[i], i))
        {
            filtered_arr.push(arr[i])
        }
    }
    return filtered_arr;
};