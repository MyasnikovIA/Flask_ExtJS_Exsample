Ext.define('Classes.Person', {
     alias: 'person', // Псевдонимы классоа
    config: {
            name: 'Eugene',
            surname : 'Popov'
    },
    constructor: function(name, surname) {
        this.initConfig();
        if(name){
            this.setName(name);
        }
        if(surname){
            this.setSurname(surname);
        }
    },
    getinfo: function(){
        alert("Полное имя : " + this.name + " " + this.surname);
    },
  });

/// Создание класса по псевдоиму
// var eugene = Ext.create('person');
// eugene.getinfo();
//
/// Классический вызов
// eugene = Ext.create('Classes.Person', 'Anders', 'Heilsberg');
// eugene.getinfo();