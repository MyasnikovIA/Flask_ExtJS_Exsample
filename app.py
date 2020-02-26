import sys
from flask import Flask
from lib.extlib1 import extlib1
from lib.extlib2 import extlib2
from lib.locale_ru import locale_ru
from lib.css.theme_classic import theme_classic


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return "render_template('error.html') ", 404


@app.route("/")
def hello():
    return """<!DOCTYPE html>
<html>
<head>
    <link href="theme_classic.css" rel="stylesheet"/>
    <script type="text/javascript" src="ext.js"></script>
    <script type="text/javascript" src="locale-ru.js"></script>
    <script type="text/javascript">
       
        Ext.onReady(function () {

            var panel1 = Ext.create('Ext.panel.Panel', {
                xtype: 'panel',
                title: 'Внутренняя панель 1',
                height: 100,
                width: '100%',
                id: "Panel1"
            });

            var panel2 = Ext.create('Ext.panel.Panel', {
                xtype: 'panel',
                title: 'Внутренняя панель 2',
                height: 600,
                width: '100%'
            });

            Ext.create('Ext.panel.Panel', {
                renderTo: Ext.getBody(),
                width: '100%',
                height: '100%',
                padding: 10,
                title: 'Основной контейнер',
                items: [panel1, panel2]
            });
            panel2.update('<h3>Вы выбрали: </h3>');
            panel2.add({
                title: 'Внутренняя панель',
                width: 300,
                height: 300,
                html: 'Привет мир!'
            });


                  var menustore = Ext.create('Ext.data.TreeStore', {
                      root: {
                          text: "Языки программирования",
                          expanded: true,
                          children: [{
                              text: "C#",
                              leaf: true
                          }, {
                              text: "C++",
                              leaf: true
                          }, {
                              text: "Java",
                              leaf: true
                          }]
                      }
                  });
                  var treemenu = Ext.create('Ext.tree.Panel', {
                      title: 'Языки программирования',
                      store: menustore,
                      width: 170,
                      rootVisible: false,
                      region: 'west',
                      listeners: {
                          itemclick: function (tree, record, item, index, e, options) {
                              var nodeText = record.data.text;
                              centerPanel.update('<h3>Вы выбрали: ' + nodeText + '</h3>');
                          }
                      }
                  });
                  var centerPanel = Ext.create('Ext.panel.Panel', {
                      title: 'Выбранный язык',
                      region: 'center'
                  });

             panel2.add(  treemenu )
             panel2.add(  centerPanel )
        });
    </script>
</head>
<body></body>
</html>"""


def jsTemp():
    txt = """ var aaa=[] ; console.log(aaa);"""
    return txt


@app.route('/<path:the_path>')
def all_other_routes(the_path):
    if (the_path == "ext.js"):
        txt = "%s%s" % (extlib1, extlib2)
        head = {'content-type': 'application/javascript; charset=utf-8', 'Content-Length': len(txt)}
        return txt, 200, head

    if (the_path == "locale-ru.js"):
        head = {'content-type': 'application/javascript; charset=utf-8', 'Content-Length': len(locale_ru)}
        return locale_ru, 200, head

    if (the_path == "theme_classic.css"):
        head = {'content-type': 'text/css; charset=utf-8', 'Content-Length': len(locale_ru)}
        return theme_classic, 200, head


    print(the_path)
    return app.send_static_file(the_path)




if __name__ == '__main__':
    try:
        port = sys.argv[1]
    except IndexError:
        port = 8080
    app.run(debug=True, host="0.0.0.0", port=port)
    # app.run( debug = True, host="0.0.0.0", port=port, ssl_context = 'adhoc')  # Generate Adhoc Certs




