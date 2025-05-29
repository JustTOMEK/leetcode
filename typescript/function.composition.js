function compose(functions) {
    return function (x) {
        var to_return = x;
        for (var i = functions.length - 1; i >= 0; i--) {
            to_return = functions[i](to_return);
        }
        return to_return;
    };
}
;
