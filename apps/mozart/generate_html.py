import os
import re

def generate_html():
    
    html = """<!DOCTYPE html>
            <html>
            <head>
                <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-beta.2/css/bootstrap.css" rel="stylesheet" type="text/css" />
                <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css" rel="stylesheet" type="text/css" />
                <script type="text/javascript" src="libraries/jquery.min.js"></script>
                <script type="text/javascript" src="libraries/jquery-ui.min.js"></script>
                <script type="text/javascript" src="libraries/bootstrap.min.js"></script>

                <script type="text/javascript">
                    setTimeout(function(){
                        console.log("I have loaded!");
                        $(".play").css("cursor", "pointer");

                        $(".play").click(function () {
                            var name = $(this).next().html();
                            console.log(name + " clicked");
                            $(".music").removeClass("playing");
                            $(this).parent().parent().addClass("playing");
                        });
                    }, 2000);
                </script>

                <style type="text/css">
                    .music-list {
                        padding: 2%;
                    }

                    .play, .lead {
                        font-size: 18pt;
                    }

                    .music {
                        margin: 1%;
                    }

                    .music-title {
                        margin-left: 0px;
                        padding-left: 0px;
                    }

                    .playing {
                        background-color: #BFB;
                    }
                </style>

                <title>Enceinte Bluetooth IoT</title>
            </head>"""
    html += """<body>
            <div class="container">
                <div class="row">
                    <div class="display-3 text-center col">Enceinte Bluetooth IoT</div>
                </div>
                <hr>
                <div class="card music-list">"""

    working_directory = os.getcwd()
    files = os.listdir("../apps/mozart/musiques")

    pattern = re.compile("^[a-zA-Z]+.mp3$")

    for f in files:
        if (pattern.match(f)):
            html+="""<div class="music">
                        <div class="row">
                            <div class="col-2"></div>
                            <div class="play col-2"><i class="fa fa-play-circle"></i></div>
                            <div class="music-title lead col-8">"""+f+"""</div>
                        </div>
                    </div>"""

    html+="""</div>
            </div>
        </body>
        </html>"""

    #print (html)

    file=open("../apps/mozart/vue.html", "w")
    file.write(html)
    file.close