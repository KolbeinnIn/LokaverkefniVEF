<div>
    <h1>Upplýsingar um leikara úr Avengers 2012</h1>
    {% if user.username == "Gestur": %}
    <h3>Velkomin/n: {{user.username}}</h3>
    <a href="/login">Skrá inn</a>
    {% else %}
    <h3>Þú ert skráð/ur inn sem: {{user.username}}</h3>
    {% endif %}
    <div class="ui three column divided grid">
        <div class="row">
        {% for key, value in leikarar.items() %}
            <div class="column">
                <a href="/leikarar/&{{key}}" class="{{key}}"><h2>{{key}}</h2></a>
                <p>{{value[0]}} ára</p>
                <p>{{value[1]}} á hæð</p>
                <p>Quote: "{{value[2]}}"</p>
                <p></p>
            </div>
        {% endfor %}
        </div>
        {% extends "leikari.tpl" %}
    </div>
</div>