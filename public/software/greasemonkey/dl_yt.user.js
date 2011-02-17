// ==UserScript==
// @name          DL YT
// @namespace     http://holizz.com/
// @description   Provides a link to "Dowload Youtube Videos"
// @include       http://www.youtube.*/*
// @include       http://youtube.*/*
// ==/UserScript==

// YouTube URL: http://www.youtube.com/watch?v=[video_id]
// YouTube download link: http://youtube.com/get_video?video_id=[video_id]&t=[t_id]

var download_url = 'http://www.downloadyoutubevideos.com/watch.php?theyturl=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D';

var ids = document.getElementsByName('video_id');
var video_id = ids[0].value;
var video_url = download_url + video_id;// + '&t=' + t_id;

// add banner with download link

var my_banner = document.createElement("div");
my_banner.innerHTML = '<div style="border-bottom: 1px solid #CCCCCC; margin-bottom: 10px; font-size: small; background-color: #FF0000; color: #FFFFFF;">' +
    '<p style="margin:0px;padding: 5px;text-align:center;">' +
    '<a href="' + video_url + '" style="color:#FFFFFF; font-weight:bold; font-size:10px;">Download Youtube Videos</a>' +
    '</p></div>';
document.body.insertBefore(my_banner, document.body.firstChild);

// clean up body margin

document.body.style.margin = '0px';
