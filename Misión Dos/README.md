### Pregunta 1: ¿Cuál es la capital de Francia?

<form id="form1">
  <input type="radio" id="madrid" name="capital" value="Madrid">
  <label for="madrid">A) Madrid</label><br>
  <input type="radio" id="paris" name="capital" value="París">
  <label for="paris">B) París</label><br>
  <input type="radio" id="londres" name="capital" value="Londres">
  <label for="londres">C) Londres</label><br>
  <input type="radio" id="berlin" name="capital" value="Berlín">
  <label for="berlin">D) Berlín</label><br>
  <button type="button" onclick="getAnswer()">Enviar Respuesta</button>
</form>

<p id="result"></p>

<script>
function getAnswer() {
  const radios = document.getElementsByName('capital');
  let selectedCapital = '';
  for (let i = 0; i < radios.length; i++) {
    if (radios[i].checked) {
      selectedCapital = radios[i].value;
      break;
    }
  }
  document.getElementById('result').innerHTML = 'Has seleccionado: ' + selectedCapital;
}
</script>
