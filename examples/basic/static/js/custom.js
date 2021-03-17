function expandChapterToc() {
  if (!window.AnimationEvent) { return; }
  var chtoc = document.getElementById('chapter-toc');
  chtoc.classList.add('expand-toc');
}

document.addEventListener('DOMContentLoaded', function() {
  if (!window.AnimationEvent) { return; }
  var anchors = document.getElementsByTagName('a');
  for (var idx=0; idx<anchors.length; idx+=1) {
    if (anchors[idx].hostname !== window.location.hostname) {
      continue;
    }
    anchors[idx].addEventListener('click', function(event) {
      var chtoc = document.getElementById('chapter-toc'),
          anchor = event.currentTarget;

      chtoc.classList.add('collapse-toc');

      event.preventDefault();

      var listener = function() {
        window.location = anchor.href;
        chtoc.removeEventListener('animationend', listener);
      };
      chtoc.addEventListener('animationend', listener);

    });
  }
});

window.addEventListener('pageshow', function (event) {
  if (!event.persisted) {
    return;
  }
  var chtoc = document.getElementById('chapter-toc');
  chtoc.classList.remove('collapse-toc');
});
