// Guide videos: show each .cp-video from its publish time on, load the YouTube player only on click.
(function () {
  document.querySelectorAll('.cp-video[data-yt]').forEach(function (fig) {
    if (Date.now() < Date.parse(fig.getAttribute('data-publish'))) return;
    fig.hidden = false;
    var btn = fig.querySelector('.cp-video-btn');
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
