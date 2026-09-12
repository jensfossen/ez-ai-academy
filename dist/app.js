(function () {
  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var area = document.createElement("textarea");
      area.value = text;
      area.setAttribute("readonly", "");
      area.style.position = "fixed";
      area.style.left = "-9999px";
      document.body.appendChild(area);
      area.select();
      try {
        document.execCommand("copy");
        resolve();
      } catch (err) {
        reject(err);
      } finally {
        document.body.removeChild(area);
      }
    });
  }

  document.querySelectorAll(".copy-btn").forEach(function (button) {
    button.addEventListener("click", function () {
      var value = button.getAttribute("data-copy") || "";
      copyText(value).then(function () {
        var previous = button.textContent;
        button.textContent = "Copied";
        button.classList.add("copied");
        window.setTimeout(function () {
          button.textContent = previous;
          button.classList.remove("copied");
        }, 2200);
      }).catch(function () {
        button.textContent = "Copy failed";
      });
    });
  });

  var toggles = Array.prototype.slice.call(document.querySelectorAll(".harness-toggle"));

  function setExpanded(button, open) {
    var panel = document.getElementById(button.getAttribute("aria-controls"));
    button.setAttribute("aria-expanded", open ? "true" : "false");
    if (panel) {
      if (open) {
        panel.removeAttribute("hidden");
      } else {
        panel.setAttribute("hidden", "");
      }
    }
  }

  function expandOnly(target) {
    toggles.forEach(function (button) {
      setExpanded(button, button === target);
    });
  }

  toggles.forEach(function (button) {
    button.addEventListener("click", function () {
      var open = button.getAttribute("aria-expanded") === "true";
      if (open) {
        setExpanded(button, false);
      } else {
        expandOnly(button);
      }
    });
  });

  function expandFromHash() {
    var id = (window.location.hash || "").replace("#", "");
    if (!id) return;
    var article = document.getElementById(id);
    if (!article || !article.classList.contains("harness")) return;
    var button = article.querySelector(".harness-toggle");
    if (button) expandOnly(button);
  }

  expandFromHash();
  window.addEventListener("hashchange", expandFromHash);

  var infoButtons = Array.prototype.slice.call(document.querySelectorAll(".info-btn"));

  function closeTips(except) {
    infoButtons.forEach(function (button) {
      if (button === except) return;
      var tip = document.getElementById(button.getAttribute("aria-controls"));
      button.setAttribute("aria-expanded", "false");
      if (tip) tip.setAttribute("hidden", "");
    });
  }

  infoButtons.forEach(function (button) {
    button.addEventListener("click", function (event) {
      event.stopPropagation();
      var tip = document.getElementById(button.getAttribute("aria-controls"));
      var open = button.getAttribute("aria-expanded") === "true";
      closeTips(button);
      button.setAttribute("aria-expanded", open ? "false" : "true");
      if (tip) {
        if (open) {
          tip.setAttribute("hidden", "");
        } else {
          tip.removeAttribute("hidden");
        }
      }
    });
  });

  document.addEventListener("click", function () {
    closeTips();
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") closeTips();
  });

  var overview = document.querySelector(".overview");
  var pauseBtn = document.querySelector(".hero-pause");
  if (overview && pauseBtn && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    pauseBtn.addEventListener("click", function () {
      var paused = overview.classList.toggle("hero-paused");
      pauseBtn.setAttribute("aria-pressed", paused ? "true" : "false");
      pauseBtn.textContent = paused ? "Play background" : "Pause background";
    });
  }
})();
