<div class="ui blue inverted segment">
    <h1>Lausar stofur</h1>
</div>
<div class="ui blue inverted segment" id="example1">
    <div class="right ui rail">
        <div class="ui sticky segment" style="width: 200px !important; height: 100px !important; left: 274.5px;">
            <h3 class="ui header">Sér valinn tími</h3>
            <form action="val">
                <div class="ui blue inverted segment">
                    <small>Ef ýtt er á X þá er núverandi tími valinn</small>
                    <input style="position: relative; left:16px; margin:5px;" id="select_time" type="time" name="timi" value="12:00" min="08:10" max="19:30">
                    <span style="position: relative; left:16px;" class="validity"></span>
                    <select  style="margin:5px;" name="dagur" required>
                        <option value=0>Dagur</option>
                        <option value=1>mánudagur</option>
                        <option value=2>þriðjudagur</option>
                        <option value=2>miðvikudagur</option>
                        <option value=3>fimmtudagur</option>
                        <option value=4>föstudagur</option>
                        <option value=5>laugardagur</option>
                    </select>
                    <select  style="margin:5px;" name="bygging" value="0">
                        <option value=0>Bygging</option>
                        <option value=1>Skólavörðuholt - aðal</option>
                        <option value=2>Tækniskólinn Hafnarfirði</option>
                        <option value=3>Sjómannaskólinn</option>
                        <option value=4>Vörðuskóli</option>
                    </select>
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
                <h4>{{dagar[x[3]-1]}}  {{x[2][0]}}:{{x[2][1]}}-{{x[2][2]}}:{{x[2][3]}}</h4>
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
                <h2>Ekkert fannst</h2>
            </div>
        {% endif %}
    </div>
    {% if flag == True: %}
    <a href="/"><button style="margin-top: 13px;">Til baka</button></a>
    {% endif %}
</div>
        
<script>
    $('.ui.sticky')
        .sticky({
        context: '#example1'
    });
</script>