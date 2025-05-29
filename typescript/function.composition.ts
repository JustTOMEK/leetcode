type F = (x: number) => number;

function compose(functions: F[]): F {

    return function(x) {
        let to_return : number = x;
        for (let i : number = functions.length - 1; i >= 0; i --)
        {
            to_return = functions[i](to_return)
        }
        return to_return;
    }
};