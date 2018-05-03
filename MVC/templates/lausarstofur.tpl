<div class="ui blue inverted segment">
    <h1>Lausar stofur</h1>
</div>
<div class="ui blue inverted segment" id="example1">
    <div class="right ui rail">
        <div class="ui sticky segment" style="width: 200px !important; height: 100px !important; left: 274.5px;">
            <h3 class="ui header">Sér valinn tími</h3>
            <form action="val">
                <div class="ui blue inverted segment">
                    <input style="position: relative; left:16px;" id="select_time" type="time" name="timi" value="12:00" min="08:10" max="19:30" required>
                    <span style="position: relative; left:16px;" class="validity"></span>
                </div>
                <div>
                    <input type="submit" value="Staðfesta">
                </div>
            </form>
        </div>
    </div>
    <div>
        {% if len != 0: %}
            {% for x in timi: %}
            <div class="ui segment">
                <h3>{{x[0]}}</h3>
                <h4>{{x[2][0]}}:{{x[2][1]}}-{{x[2][2]}}:{{x[2][3]}}</h4>
                {% if x[-1] == 1: %}
                    <h4 style="margin:0;">{{byggingar[0][1]}}</h4>
                    <h4 style="margin:0;">{{byggingar[0][2]}}</h4>
                {% elif x[-1] == 2: %}
                    <h4 style="margin:0;">{{byggingar[1][1]}}</h4>
                    <h4 style="margin:0;">{{byggingar[1][2]}}</h4>
                {% elif x[-1] == 3: %}
                    <h4 style="margin:0;">{{byggingar[2][1]}}</h4>
                    <h4 style="margin:0;">{{byggingar[2][2]}}</h4>
                {% elif x[-1] == 4: %}
                    <h4 style="margin:0;">{{byggingar[3][1]}}</h4>
                    <h4 style="margin:0;">{{byggingar[3][2]}}</h4>
                {% else: %}
                    <h4>Bygging óvituð</h4>
                {% endif %}
            </div>
            {% endfor %}
        
        {% else: %}
            <div class="ui segment">
                <h2>Allar stofur eru lausar.</h2>
                <p>Það er pása</p>
            </div>
        {% endif %}
    </div>
    {% if flag == True: %}
    <a href="/"><button>Til baka</button></a>
    {% endif %}
</div>
        
<script>
    $('.ui.sticky')
        .sticky({
        context: '#example1'
    });
</script>