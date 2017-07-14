function onOpen() {
  var menu = SpreadsheetApp.getUi().createMenu('Update bot')
 
   
menu.addItem('I am ready to update', 'menuItem1')
 .addSeparator()
 .addSubMenu(SpreadsheetApp.getUi().createMenu('Helpful information')
 .addItem('Important rules', 'menuItem2')
 .addSeparator()
 .addItem('In case of an error', 'menuItem3'))
 .addToUi();         
}

function menuItem1() {
  
  
  if (checkFields() == 1) {
  var options = {"method" : 'GET'};
  var url ="http://innolinksbot.pythonanywhere.com/update";
  try {
  var response = UrlFetchApp.fetch(url, options);
  var code = response.getResponseCode()
  var text = response.getContentText()
  
  Logger.log("response code: "+code);
  Logger.log("response: "+text);
  
  SpreadsheetApp.getUi()
  .alert(text);
  }
  catch(e) {
    var error = e.message
    SpreadsheetApp.getUi()
    .alert("There are some problems with access to Google Spreadsheets. Could you try again later?\n\n"+error)
  
    }
  }
}

function menuItem2() {
  SpreadsheetApp.getUi() 
  .alert('❗️ Before you decide to update the bot, please check if \n the lines you changed contain three neccessary fields:\n\n ✔️ card_title\n ✔️ category\n ✔️ subcategory\n\n Our bot can`t live without them :)');
}

function menuItem3() {
  SpreadsheetApp.getUi() 
  .alert('If something went wrong... Just keep calm and try again a bit later.\n There are some temporary problems with internet connection.');
}


function checkFields() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var data = sheet.getDataRange().getValues();
  var result = 1;
  for (var i = 0; i < data.length; i++) {
    if  (data[i][0].toString()==''||data[i][1].toString()==''||data[i][2].toString()==''){
      SpreadsheetApp.getUi()
    .alert("Please fill all the neccessary fields")
     return result = 0;
    }
    
  }
  Logger.log("result is " + result);
  return result
}



function RemoveMenu() {
     var ss = SpreadsheetApp.getActiveSpreadsheet();
     ss.removeMenu('My Custom Menu');
}



