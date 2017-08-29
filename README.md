# PyDictionary
This project is a simple module to create a soft dictionary which accepts a word from the user and results the meaning of word.<br>
<b><br>Features:<br><ul><li>pydictionary is not case sensitive.<li>supports spelling errors<br></ul></b>

<b>Usage:</b><br><br>
import pydictionary
<br>
data= pydictionary.load_data('data.json')
<br>
print pydictionary.get_meaning('RaIn',data)
<br>
<br>
<b><br>Output:</b><br>
<p>['rain', u'Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.']</p>
     
    
