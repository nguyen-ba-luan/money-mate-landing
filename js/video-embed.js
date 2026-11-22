// Guide videos: show the poster; clicking it loads the YouTube player in place.
(function () {
  document.querySelectorAll('.cp-video[data-yt]').forEach(function (fig) {
    var btn = fig.querySelector('.cp-video-btn');
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
