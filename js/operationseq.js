//https://www.codewars.com/kata/5e4bb05b698ef0001e3344bc/
var BN = require("bignumber.js");
function solve(arr) {
    //(a^2 + b^2)(c^2 + d^2) = (ac-bd)^2 + (ad+bc)^2
    // for 4 elements in arr that's all
    // for more:
    // (a^2 + b^2)(c^2 + d^2)(e^2 + f^2) = ((ac-bd)^2 + (ad+bc)^2)(e^2 + f^2) ==>
    // ac-bd is new a
    // ad+bc is new b
    // take first a,b,c,d to get (ac-bd)^2 + (ad+bc)^2 as
    // a and b for next
    var ac_bd = BigInt(Math.abs(arr[0] * arr[2] - arr[1] * arr[3]));
    var ad_bc = BigInt(Math.abs(arr[0] * arr[3] + arr[1] * arr[2]));
    // Now we must take c and d
    for (var i = 4; i < arr.length; i += 2) {
        // we have ((ac_bd)^2 + (ad+bc)^2)(e^2 + f^2)
        // represent it as (a^2 + b^2)(c^2 + d^2) = (ac-bd)^2 + (ad+bc)^2
        // now ac_bd is a
        // ad_bc is b
        var new_ac_bd = BigInt(ac_bd * BigInt(arr[i]) - ad_bc * BigInt(arr[i + 1]));
        var new_ad_bc = BigInt(ac_bd * BigInt(arr[i + 1]) + ad_bc * BigInt(arr[i]));
        ac_bd = new_ac_bd > 0 ? new_ac_bd : new_ac_bd * BigInt(-1);
        ad_bc = new_ad_bc > 0 ? new_ad_bc : new_ad_bc * BigInt(-1);
    }
    return [ac_bd, ad_bc];
}
//# sourceMappingURL=operationseq.js.map