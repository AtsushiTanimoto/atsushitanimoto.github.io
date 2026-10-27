// data-u / data-d(文字列を反転したもの)からメールアドレスを組み立てて mailto リンクにする
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".js-email").forEach(function (el) {
    var rev = function (s) { return s.split("").reverse().join(""); };
    var addr = rev(el.dataset.u) + "@" + rev(el.dataset.d);
    var a = document.createElement("a");
    a.href = "mailto:" + addr;
    a.textContent = addr;
    el.replaceWith(a);
  });
});
