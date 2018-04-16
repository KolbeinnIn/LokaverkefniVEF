{% if uppl != "": %}
<div class="ui modal">
    <h1>{{uppl[-1]}}</h1>
    <p>{{uppl[0]}}. ára</p>
    <p>{{uppl[1]}} á hæð</p>
    <p>Quote: "{{uppl[2]}}"</p>
</div>
<script>
    $('.ui.modal').modal('show');
</script>
{% endif %}