"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Kata = /** @class */ (function () {
    function Kata() {
    }
    Kata.highAndLow = function (numbers) {
        var arrayOfNumbers = numbers
            .split(' ')
            .map(function (str) { return parseInt(str); })
            .sort(function (a, b) { return a - b; });
        return arrayOfNumbers.[arrayOfNumbers.length - 1] + " " + arrayOfNumbers[0];
    };
    return Kata;
}());
exports.Kata = Kata;
