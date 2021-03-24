window.onscroll = function() {
    var onPage = [];

    var anchors = document.querySelectorAll('#sidebarNav a');
    for (var i = 0; i < anchors.length; ++i) {
        anchors[i].classList.remove('active');
        var href = anchors[i].getAttribute('href').split('#');
        if (href[0] == window.location.pathname) {
            var hrefElemTop = document.getElementById(href[1]).getBoundingClientRect().top;
            onPage.push([anchors[i], hrefElemTop]);
        }
    }

    var activeAnchor = null;
    if (window.pageYOffset == 0) {
        activeAnchor = onPage[0][0];
    } else if ((window.innerHeight + window.pageYOffset) > document.body.offsetHeight) {
        activeAnchor = onPage[onPage.length - 1][0];
    } else {
        for (var i = 0; i < onPage.length; ++i) {
            var anchor = onPage[i][0];
            var top = onPage[i][1];

            if (top < 0.15 * window.innerHeight) {
                activeAnchor = anchor;
            }
        }
    }
    activeAnchor.classList.add('active');
};
