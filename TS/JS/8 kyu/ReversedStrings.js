"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function solution(str) {
    if (str != '') {
        var reversed = '';
        for (var i = str.length - 1; i >= 0; i--) {
            reversed += String(str.charAt(i));
        }
        return reversed;
    }
    return '';
}
exports.solution = solution;
function MuchBetter(str) {
    return str.split('').reverse().join('');
}
exports.MuchBetter = MuchBetter;
