<?php header('Content-type: text/html; charset=UTF-8') ?>
<!DOCTYPE html>
<title>Ruby support with CSS</title>
<style type="text/css">
ruby, rb, rt, rp
{
  display: inline;
}

ruby
{
  /* DEBUGGING */
  outline: 1px solid red;
}

rb
{
  clear: both;
  float: left;
  /* DEBUGGING */
  /*text-decoration: overline;*/
  outline: 1px solid lime;
}

rt
{
  clear: both;
  float: left;
  font-size: 0.5em;
  /* DEBUGGING */
  /*text-decoration: underline;*/
  outline: 1px solid blue;
}

rp
{
  display: none;
}
</style>
<p lang="ja">あなたは<ruby><rb>猫</rb><rp>（</rp><rt>ねこ</rt><rp>）</rp></ruby>ですか。<ruby><rb>今日</rb><rp>（</rp><rt>こんにち</rt><rp>）</rp></ruby>は、<ruby><rb>猫</rb><rp>（</rp><rt>ねこ</rt><rp>）</rp></ruby>さん。
