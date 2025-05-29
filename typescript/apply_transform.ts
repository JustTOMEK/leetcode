function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    let return_array : number[] = [];
    for (let i : number = 0; i < arr.length; i++)
    {
        return_array.push(fn(arr[i], i));
    }
    return return_array;
};