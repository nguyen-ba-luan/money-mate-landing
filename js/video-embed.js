// Guide videos: before the publish time a .cp-video stays hidden, or with data-soon shows its poster
// labelled "coming"; from the publish time on, clicking it loads the YouTube player.
(function () {
  document.querySelectorAll('.cp-video[data-yt]').forEach(function (fig) {
    var btn = fig.querySelector('.cp-video-btn');
    if (Date.now() < Date.parse(fig.getAttribute('data-publish'))) {
      if (fig.hasAttribute('data-soon')) { fig.classList.add('is-soon'); btn.disabled = true; }
      return;
    }
    fig.hidden = false;
    btn.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + fig.getAttribute('data-yt') + '?autoplay=1&rel=0';
      f.title = btn.getAttribute('aria-label');
      f.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture';
      f.allowFullscreen = true;
      btn.replaceWith(f);
    });
  });
})();
