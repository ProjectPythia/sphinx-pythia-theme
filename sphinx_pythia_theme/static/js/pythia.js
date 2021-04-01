window.onscroll = function() {
    var onPage = [];

    var anchors = document.querySelectorAll('#sidebarNavItems a');
    if (anchors.length == 0) {
        return;
    }
    for (var i = 0; i < anchors.length; ++i) {
        anchors[i].classList.remove('active');
        var href = anchors[i].getAttribute('href').split('#');
        if (href.length > 1 && href[0] == '') {
            var ref_id = null;
            if (href[1] == '') {
                ref_id = document.querySelector('#main div.section').getAttribute('id');
            } else {
                ref_id = href[1];
            }
            var hrefElemTop = document.getElementById(ref_id).getBoundingClientRect().top;
            onPage.push([anchors[i], hrefElemTop]);
        }
    }

    var activeAnchor = null;
    if (window.pageYOffset == 0) {
        activeAnchor = onPage[0][0];
    } else if ((window.innerHeight + window.pageYOffset) >= document.body.offsetHeight - 10) {
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

var bp = getComputedStyle(document.documentElement).getPropertyValue('--main-contract-breakpoint');
const mediaQuery = window.matchMedia( '(min-width: ' + bp + ')' );
document.addEventListener("DOMContentLoaded", function(event) {
    if (!mediaQuery.matches) {
        var cIcon = document.getElementById('contractIcon');
        cIcon.classList.remove('bi-chevron-contract');
        cIcon.classList.add('bi-chevron-expand');
    }
});

function contractSidebar() {
    var sidebarLeft = getComputedStyle(document.documentElement).getPropertyValue('--sidebar-left-contracted');
    document.getElementById('sidebar').style.left = sidebarLeft;

    var sidebarNav = document.getElementById('sidebarNav');
    var sidebarNavHeight = sidebarNav.scrollHeight;
    var sidebarNavTransition = sidebarNav.style.transition;
    sidebarNav.style.transition = '';
    requestAnimationFrame(function() {
        sidebarNav.style.height = sidebarNavHeight + 'px';
        sidebarNav.style.transition = sidebarNavTransition;
        requestAnimationFrame(function() {
            sidebarNav.style.height = 2 + 'rem';
        });
    });

    document.getElementById('contractIcon').classList.remove('bi-chevron-contract');
    document.getElementById('contractIcon').classList.add('bi-chevron-expand');

    if (mediaQuery.matches) {
        var mainMarginLeft = getComputedStyle(document.documentElement).getPropertyValue('--main-margin-left-contracted');
        document.getElementById('main').style.marginLeft = mainMarginLeft;
    }
}

function expandSidebar() {
    var sidebarLeft = getComputedStyle(document.documentElement).getPropertyValue('--sidebar-left-expanded');
    document.getElementById('sidebar').style.left = sidebarLeft;

    var sidebarNav = document.getElementById('sidebarNav');
    var sidebarNavHeight = sidebarNav.scrollHeight;
    sidebarNav.style.height = sidebarNavHeight + 'px';
    sidebarNav.addEventListener('transitionend', function(e) {
        sidebarNav.removeEventListener('transitionend', arguments.callee);
        sidebarNav.style.height = null;
    });

    document.getElementById('contractIcon').classList.remove('bi-chevron-expand');
    document.getElementById('contractIcon').classList.add('bi-chevron-contract');

    if (mediaQuery.matches) {
        var mainMarginLeft = getComputedStyle(document.documentElement).getPropertyValue('--main-margin-left-expanded');
        document.getElementById('main').style.marginLeft = mainMarginLeft;
    }
}

function toggleSidebar() {
    var sidebar = document.getElementById('sidebar');
    var sidebarLeft = window.getComputedStyle(sidebar, null).getPropertyValue('left');
    var sidebarLeftpx = parseInt(sidebarLeft.substring(0, sidebarLeft.length - 2));
    var isContracted = sidebarLeftpx < -10;

    if (isContracted) {
        expandSidebar();
    } else {
        contractSidebar();
    }
}
