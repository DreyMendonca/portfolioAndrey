// Campo de estrelas com brilho suave e estrelas cadentes ocasionais.
(function () {
  var c = document.getElementById("stars");
  if (!c || !c.getContext) return;
  var ctx = c.getContext("2d");
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var stars = [], shooting = null, w, h, dpr;

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = c.clientWidth; h = c.clientHeight;
    c.width = w * dpr; c.height = h * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var n = Math.round((w * h) / 2600);
    stars = [];
    for (var i = 0; i < n; i++) {
      stars.push({
        x: Math.random() * w, y: Math.random() * h,
        r: Math.random() < 0.92 ? Math.random() * 0.9 + 0.2 : Math.random() * 1.2 + 1,
        a: Math.random() * 0.7 + 0.2, s: Math.random() * 0.02 + 0.004, p: Math.random() * Math.PI * 2,
        v: Math.random() * 0.04 + 0.01
      });
    }
  }

  function draw(t) {
    ctx.clearRect(0, 0, w, h);
    for (var i = 0; i < stars.length; i++) {
      var s = stars[i];
      if (!reduce) { s.y += s.v; if (s.y > h) s.y = 0; }
      var a = reduce ? s.a : s.a * (0.6 + 0.4 * Math.sin(t * s.s * 0.06 + s.p));
      ctx.globalAlpha = a;
      ctx.fillStyle = "#fff";
      ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2); ctx.fill();
    }
    if (!reduce) {
      if (!shooting && Math.random() < 0.003) {
        shooting = { x: Math.random() * w * 0.7, y: Math.random() * h * 0.4, l: 0 };
      }
      if (shooting) {
        shooting.l += 1;
        var len = 80, x = shooting.x + shooting.l * 9, y = shooting.y + shooting.l * 4;
        var g = ctx.createLinearGradient(x, y, x - len, y - len * 0.45);
        g.addColorStop(0, "rgba(255,255,255,0.9)"); g.addColorStop(1, "rgba(255,255,255,0)");
        ctx.globalAlpha = Math.max(0, 1 - shooting.l / 40);
        ctx.strokeStyle = g; ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x - len, y - len * 0.45); ctx.stroke();
        if (shooting.l > 40) shooting = null;
      }
      requestAnimationFrame(draw);
    }
    ctx.globalAlpha = 1;
  }

  window.addEventListener("resize", resize);
  resize();
  requestAnimationFrame(draw);
})();
