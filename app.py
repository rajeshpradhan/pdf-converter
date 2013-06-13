  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>python-amqp-example/app.py at master · cloudamqp/python-amqp-example</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="http://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <link rel="assets" href="https://a248.e.akamai.net/assets.github.com/">
    <link rel="xhr-socket" href="/_sockets" />
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="244896" name="octolytics-actor-id" /><meta content="rajeshpradhan" name="octolytics-actor-login" /><meta content="1973d0ff10c84f28d7d36849db9301c6b1b068f834b7f14c0ebdd556e311f299" name="octolytics-actor-hash" />

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="29QunflUSLmM8fE2jjdsEVdbbZIa3+3jAOp4pW9qIIw=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-e0839eb5a977102e725aa4bdf08677ab94f33a1d.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-73ebb666638c4732164fe0b708d174c2e1012934.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-4c434fa1705bf526e191eec0cd8fab1a5ce3e326.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-367f72c94a10a3b7f74ed5adf36d4ca50c205114.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="4ea724a5ab998ddf6e34b864fe5b455c">

        <link data-pjax-transient rel='permalink' href='/cloudamqp/python-amqp-example/blob/d969f20746f474e9f76843a33b558fcb9ee00b83/app.py'>
    <meta property="og:title" content="python-amqp-example"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/cloudamqp/python-amqp-example"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/b77d1c815eb4c695738cbe9e2e436195?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="python-amqp-example - How to connect from Python to CloudAMQP"/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="cloudamqp/python-amqp-example"/>

    <meta name="description" content="python-amqp-example - How to connect from Python to CloudAMQP" />


    <meta content="1513401" name="octolytics-dimension-user_id" /><meta content="cloudamqp" name="octolytics-dimension-user_login" /><meta content="3843799" name="octolytics-dimension-repository_id" /><meta content="cloudamqp/python-amqp-example" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="3843799" name="octolytics-dimension-repository_network_root_id" /><meta content="cloudamqp/python-amqp-example" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/cloudamqp/python-amqp-example/commits/master.atom" rel="alternate" title="Recent Commits to python-amqp-example:master" type="application/atom+xml" />

  </head>


  <body class="logged_in page-blob macintosh vis-public env-production  ">
    <div id="wrapper">

      
      
      

      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/organizations/eshares">
  <span class="mega-octicon octicon-mark-github"></span>
</a>

    <div class="divider-vertical"></div>

    
  <a href="/notifications" class="notification-indicator tooltipped downwards" title="You have unread notifications">
    <span class="mail-status unread"></span>
  </a>
  <div class="divider-vertical"></div>


      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">
  <a href="/search/advanced" class="advanced-search-icon tooltipped downwards command-bar-search" id="advanced_search" title="Advanced search"><span class="octicon octicon-gear "></span></a>

  <input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    data-username="rajeshpradhan"
      data-repo="cloudamqp/python-amqp-example"
      data-branch="master"
      data-sha="1d94dd8a68c0f2663bf6741ba06cc0de990b37c7"
  >

    <input type="hidden" name="nwo" value="cloudamqp/python-amqp-example" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

  <div class="divider-vertical"></div>

</form>
        <ul class="top-nav">
            <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="http://help.github.com">Help</a></li>
        </ul>
      </div>

    

  

    <ul id="user-links">
      <li>
        <a href="/rajeshpradhan" class="name">
          <img height="20" src="https://secure.gravatar.com/avatar/9e8f372e91cc6a38e1cfa43d79d0cada?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /> rajeshpradhan
        </a>
      </li>

        <li>
          <a href="/new" id="new_repo" class="tooltipped downwards" title="Create a new repo">
            <span class="octicon octicon-repo-create"></span>
          </a>
        </li>

        <li>
          <a href="/settings/profile" id="account_settings"
            class="tooltipped downwards"
            title="Account settings ">
            <span class="octicon octicon-tools"></span>
          </a>
        </li>
        <li>
          <a class="tooltipped downwards" href="/logout" data-method="post" id="logout" title="Sign out">
            <span class="octicon octicon-log-out"></span>
          </a>
        </li>

    </ul>


<div class="js-new-dropdown-contents hidden">
  <ul class="dropdown-menu">
    <li>
      <a href="/new"><span class="octicon octicon-repo-create"></span> New repository</a>
    </li>
    <li>
        <a href="/cloudamqp/python-amqp-example/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
    </li>
    <li>
    </li>
    <li>
      <a href="/organizations/new"><span class="octicon octicon-list-unordered"></span> New organization</a>
    </li>
  </ul>
</div>


    
  </div>
</div>

      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu ">
          <div class="container">
            <div class="title-actions-bar">
              

<ul class="pagehead-actions">


    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="29QunflUSLmM8fE2jjdsEVdbbZIa3+3jAOp4pW9qIIw=" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="3843799" />

    <div class="select-menu js-menu-container js-select-menu">
      <span class="minibutton select-menu-button  js-menu-target">
        <span class="js-select-button">
          <span class="octicon octicon-eye-watch"></span>
          Watch
        </span>
      </span>

      <div class="select-menu-modal-holder js-menu-content">
        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container">

            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for discussions in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-watch"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

    <li class="js-toggler-container js-social-container starring-container ">
      <a href="/cloudamqp/python-amqp-example/unstar" class="minibutton with-count js-toggler-target star-button starred upwards" title="Unstar this repo" data-remote="true" data-method="post" rel="nofollow">
        <span class="octicon octicon-star-delete"></span>
        <span class="text">Unstar</span>
      </a>
      <a href="/cloudamqp/python-amqp-example/star" class="minibutton with-count js-toggler-target star-button unstarred upwards" title="Star this repo" data-remote="true" data-method="post" rel="nofollow">
        <span class="octicon octicon-star"></span>
        <span class="text">Star</span>
      </a>
      <a class="social-count js-social-count" href="/cloudamqp/python-amqp-example/stargazers">3</a>
    </li>

        <li>
          <a href="/cloudamqp/python-amqp-example/fork" class="minibutton with-count js-toggler-target fork-button lighter upwards" title="Fork this repo" rel="facebox nofollow">
            <span class="octicon octicon-git-branch-create"></span>
            <span class="text">Fork</span>
          </a>
          <a href="/cloudamqp/python-amqp-example/network" class="social-count">0</a>
        </li>


</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-octicon octicon-repo"></span>
                <span class="author vcard">
                  <a href="/cloudamqp" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">cloudamqp</span>
                  </a></span> /
                <strong><a href="/cloudamqp/python-amqp-example" class="js-current-repository">python-amqp-example</a></strong>
              </h1>
            </div>

            
  <ul class="tabs">
    <li class="pulse-nav"><a href="/cloudamqp/python-amqp-example/pulse" class="js-selected-navigation-item " data-selected-links="pulse /cloudamqp/python-amqp-example/pulse" rel="nofollow"><span class="octicon octicon-pulse"></span></a></li>
    <li><a href="/cloudamqp/python-amqp-example" class="js-selected-navigation-item selected" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /cloudamqp/python-amqp-example">Code</a></li>
    <li><a href="/cloudamqp/python-amqp-example/network" class="js-selected-navigation-item " data-selected-links="repo_network /cloudamqp/python-amqp-example/network">Network</a></li>
    <li><a href="/cloudamqp/python-amqp-example/pulls" class="js-selected-navigation-item " data-selected-links="repo_pulls /cloudamqp/python-amqp-example/pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/cloudamqp/python-amqp-example/issues" class="js-selected-navigation-item " data-selected-links="repo_issues /cloudamqp/python-amqp-example/issues">Issues <span class='counter'>0</span></a></li>

      <li><a href="/cloudamqp/python-amqp-example/wiki" class="js-selected-navigation-item " data-selected-links="repo_wiki /cloudamqp/python-amqp-example/wiki">Wiki</a></li>


    <li><a href="/cloudamqp/python-amqp-example/graphs" class="js-selected-navigation-item " data-selected-links="repo_graphs repo_contributors /cloudamqp/python-amqp-example/graphs">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/cloudamqp/python-amqp-example/tags" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_tags /cloudamqp/python-amqp-example/tags">Tags <span class="counter blank">0</span></a></li>
    </ul>
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="master">
        <span class="octicon octicon-git-branch"></span>
        <i>branch:</i>
        <span class="js-select-button">master</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">

        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
            </div>
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches">

            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item selected">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/cloudamqp/python-amqp-example/blob/master/app.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
                </div> <!-- /.select-menu-item -->
            </div>

              <div class="select-menu-no-results">Nothing to show</div>
          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags">
            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

            </div>

            <div class="select-menu-no-results">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/cloudamqp/python-amqp-example" class="selected js-selected-navigation-item tabnav-tab" data-selected-links="repo_source /cloudamqp/python-amqp-example">Files</a></li>
    <li><a href="/cloudamqp/python-amqp-example/commits/master" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_commits /cloudamqp/python-amqp-example/commits/master">Commits</a></li>
    <li><a href="/cloudamqp/python-amqp-example/branches" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_branches /cloudamqp/python-amqp-example/branches" rel="nofollow">Branches <span class="counter ">1</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:dd5228d86e309e352d1848a8225c2010 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:dd5228d86e309e352d1848a8225c2010 -->


<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <div class="breadcrumb">
          <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/cloudamqp/python-amqp-example" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">python-amqp-example</span></a></span></span><span class="separator"> / </span><strong class="final-path">app.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="app.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
        </div>

      <a href="/cloudamqp/python-amqp-example/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>


        
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/f0a3ce9ab4d65f2e2dad6cd0aa63c98a?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
    <span class="author"><a href="/carlhoerberg" rel="author">carlhoerberg</a></span>
    <time class="js-relative-date" datetime="2012-03-27T06:10:19-07:00" title="2012-03-27 06:10:19">March 27, 2012</time>
    <div class="commit-title">
        <a href="/cloudamqp/python-amqp-example/commit/d969f20746f474e9f76843a33b558fcb9ee00b83" class="message">Inital commit</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong> contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li class="facebox-user-list-item">
          <img height="24" src="https://secure.gravatar.com/avatar/f0a3ce9ab4d65f2e2dad6cd0aa63c98a?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/carlhoerberg">carlhoerberg</a>
        </li>
      </ul>
    </div>
  </div>


    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/cloudamqp/python-amqp-example/blob/d969f20746f474e9f76843a33b558fcb9ee00b83/app.py" data-title="python-amqp-example/app.py at master · cloudamqp/python-amqp-example · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="octicon octicon-file-text"></b></span>
                <span class="mode" title="File Mode">file</span>
                  <span>29 lines (21 sloc)</span>
                <span>0.951 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                        <a class="minibutton tooltipped leftwards"
                           title="Clicking this button will automatically fork this project so you can edit the file"
                           href="/cloudamqp/python-amqp-example/edit/master/app.py"
                           data-method="post" rel="nofollow">Edit</a>
                  <a href="/cloudamqp/python-amqp-example/raw/master/app.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/cloudamqp/python-amqp-example/blame/master/app.py" class="button minibutton ">Blame</a>
                  <a href="/cloudamqp/python-amqp-example/commits/master/app.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="blob-wrapper data type-python js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="kn">import</span> <span class="nn">pika</span><span class="o">,</span> <span class="nn">os</span><span class="o">,</span> <span class="nn">urlparse</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="c"># Parse CLODUAMQP_URL (fallback to localhost)</span></div><div class='line' id='LC4'><span class="n">url_str</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;CLOUDAMQP_URL&#39;</span><span class="p">,</span> <span class="s">&#39;amqp://guest:guest@localhost//&#39;</span><span class="p">)</span></div><div class='line' id='LC5'><span class="n">url</span> <span class="o">=</span> <span class="n">urlparse</span><span class="o">.</span><span class="n">urlparse</span><span class="p">(</span><span class="n">url_str</span><span class="p">)</span></div><div class='line' id='LC6'><span class="n">params</span> <span class="o">=</span> <span class="n">pika</span><span class="o">.</span><span class="n">ConnectionParameters</span><span class="p">(</span><span class="n">host</span><span class="o">=</span><span class="n">url</span><span class="o">.</span><span class="n">hostname</span><span class="p">,</span> <span class="n">virtual_host</span><span class="o">=</span><span class="n">url</span><span class="o">.</span><span class="n">path</span><span class="p">[</span><span class="mi">1</span><span class="p">:],</span></div><div class='line' id='LC7'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">credentials</span><span class="o">=</span><span class="n">pika</span><span class="o">.</span><span class="n">PlainCredentials</span><span class="p">(</span><span class="n">url</span><span class="o">.</span><span class="n">username</span><span class="p">,</span> <span class="n">url</span><span class="o">.</span><span class="n">password</span><span class="p">))</span></div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'><span class="n">connection</span> <span class="o">=</span> <span class="n">pika</span><span class="o">.</span><span class="n">BlockingConnection</span><span class="p">(</span><span class="n">params</span><span class="p">)</span> <span class="c"># Connect to CloudAMQP</span></div><div class='line' id='LC10'><span class="n">channel</span> <span class="o">=</span> <span class="n">connection</span><span class="o">.</span><span class="n">channel</span><span class="p">()</span> <span class="c"># start a channel</span></div><div class='line' id='LC11'><span class="n">channel</span><span class="o">.</span><span class="n">queue_declare</span><span class="p">(</span><span class="n">queue</span><span class="o">=</span><span class="s">&#39;hello&#39;</span><span class="p">)</span> <span class="c"># Declare a queue</span></div><div class='line' id='LC12'><span class="c"># send a message</span></div><div class='line' id='LC13'><span class="n">channel</span><span class="o">.</span><span class="n">basic_publish</span><span class="p">(</span><span class="n">exchange</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">,</span> <span class="n">routing_key</span><span class="o">=</span><span class="s">&#39;hello&#39;</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="s">&#39;Hello CloudAMQP!&#39;</span><span class="p">)</span></div><div class='line' id='LC14'><span class="k">print</span> <span class="s">&quot; [x] Sent &#39;Hello World!&#39;&quot;</span></div><div class='line' id='LC15'><br/></div><div class='line' id='LC16'><span class="c"># create a function which is called on incoming messages</span></div><div class='line' id='LC17'><span class="k">def</span> <span class="nf">callback</span><span class="p">(</span><span class="n">ch</span><span class="p">,</span> <span class="n">method</span><span class="p">,</span> <span class="n">properties</span><span class="p">,</span> <span class="n">body</span><span class="p">):</span></div><div class='line' id='LC18'>&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot; [x] Received </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">body</span><span class="p">)</span></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><span class="c"># set up subscription on the queue</span></div><div class='line' id='LC21'><span class="n">channel</span><span class="o">.</span><span class="n">basic_consume</span><span class="p">(</span><span class="n">callback</span><span class="p">,</span></div><div class='line' id='LC22'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">queue</span><span class="o">=</span><span class="s">&#39;hello&#39;</span><span class="p">,</span></div><div class='line' id='LC23'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">no_ack</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC24'><br/></div><div class='line' id='LC25'><span class="n">channel</span><span class="o">.</span><span class="n">start_consuming</span><span class="p">()</span> <span class="c"># start consuming (blocks)</span></div><div class='line' id='LC26'><br/></div><div class='line' id='LC27'><span class="n">connection</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC28'><br/></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;">
            <button type="submit" class="button">Go</button>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif" height="64" width="64">
</div>


        </div>
      </div>
      <div class="modal-backdrop"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="/about">About us</a></dd>
        <dd><a href="/blog">Blog</a></dd>
        <dd><a href="/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.08700s from fe16.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>
    <ul id="legal">
        <li><a href="/site/terms">Terms of Service</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/cloudamqp/python-amqp-example/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="octicon octicon-remove-close ajax-error-dismiss"></a>
    </div>

    
    <span id='server_response_time' data-time='0.08745' data-host='fe16'></span>
    
  </body>
</html>

