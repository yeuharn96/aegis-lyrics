Number.prototype.round = function (precision) {
    const num = Math.round((this.valueOf() + Number.EPSILON) * Math.pow(10, precision)) / Math.pow(10, precision);
    return num.toFixed(precision);
}