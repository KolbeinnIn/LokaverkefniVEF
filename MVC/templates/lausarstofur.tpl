<div class="ui segment">
    <div class="b ui segment">
        <h1 style="color:white; text-shadow: 1px 1px black;">Lausar stofur</h1>
    </div>
    <div class="b ui segment" id="val">
        <div class="ui four column grid">    
            <div class="desktop-only computer only large screen only sixteen wide column">
                <div class="right ui rail" style="left:770px !important">
                    <div class="ui sticky segment">
                        <h3 class="ui header">Sér valinn tími</h3>
                        <form action="val">
                            <div class="b ui segment">
                                <small>Ef ýtt er á X þá er núverandi tími valinn</small>
                                <input style="position: relative; left:16px; margin:5px;" id="select_time" type="time" name="timi" value="12:00" min="08:10" max="19:30">
                                <span style="position: relative; left:16px;" class="validity"></span>
                                <select  style="margin:5px;" name="dagur" required>
                                    <option value=0>Dagur</option>
                                    <option value=1>mánudagur</option>
                                    <option value=2>þriðjudagur</option>
                                    <option value=3>miðvikudagur</option>
                                    <option value=4>fimmtudagur</option>
                                    <option value=5>föstudagur</option>
                                    <option value=6>laugardagur</option>
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
                        {% if flag == True: %}
                        <a href="/"><button style="margin-top: 13px;">Til baka</button></a>
                        {% endif %}
                    </div>
                </div>
            </div>
            <div class="asdf large screen only sixteen wide column">
                <div class="right ui rail" style="left:770px !important">
                    <div class="ui sticky segment">
                        <h3 class="ui header">Sér valinn tími</h3>
                        <form action="val">
                            <div class="b ui segment">
                                <small>Ef ýtt er á X þá er núverandi tími valinn</small>
                                <input style="position: relative; left:16px; margin:5px;" id="select_time" type="time" name="timi" value="12:00" min="08:10" max="19:30">
                                <span style="position: relative; left:16px;" class="validity"></span>
                                <select  style="margin:5px;" name="dagur" required>
                                    <option value=0>Dagur</option>
                                    <option value=1>mánudagur</option>
                                    <option value=2>þriðjudagur</option>
                                    <option value=3>miðvikudagur</option>
                                    <option value=4>fimmtudagur</option>
                                    <option value=5>föstudagur</option>
                                    <option value=6>laugardagur</option>
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
                        {% if flag == True: %}
                        <a href="/"><button style="margin-top: 13px;">Til baka</button></a>
                        {% endif %}
                    </div>
                </div>
            </div>
            <div class="sma sixteen wide column">
                <div class="ui segment" style="margin-bottom: 15px;">
                    <h3 class="ui header">Sér valinn tími</h3>
                    <form action="val">
                        <div class="b ui segment">
                            <small>Ef enginn tími er valinn þá er núverandi tími notaður</small>
                            <br>
                            <input style="position: relative; left:16px; margin:5px;" id="select_time" type="time" name="timi" min="08:10" max="19:30">
                            <span style="position: relative; left:16px;" class="validity"></span>
                            <br>
                            <select  style="margin:5px;" name="dagur" required>
                                <option value=0>Dagur</option>
                                <option value=1>mánudagur</option>
                                <option value=2>þriðjudagur</option>
                                <option value=3>miðvikudagur</option>
                                <option value=4>fimmtudagur</option>
                                <option value=5>föstudagur</option>
                                <option value=6>laugardagur</option>
                            </select>
                            <br>
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
                    {% if flag == True: %}
                    <a href="/"><button style="margin-top: 13px;">Til baka</button></a>
                    {% endif %}
                </div>
            </div>
        </div>
        
        <div>
            <div class="ui segment">
                <h2>Klukkan asder: &nbsp;{{klst}}:{{minu}}</h2>
            </div>
            {% if lengd != 0: %}
                {% if timi[0][0] == "Pása":%}
                    <div class="ui segment">
                        <h3>Allar stofur eru lausar frá</h3>
                        {% for x in range(len): %}
                            <h4>kl {{timi[x][2][0]}}:{{timi[x][2][1]}} - {{timi[x][2][2]}}:{{timi[x][2][3]}}</h4>
                        {% endfor %}
                    </div>
                {% else %}
                    {% for x in timi:%}
                    <div class="ui segment">
                        <h3>{{x[0]}}</h3>
                        {% if x[3] == 7: %}
                            <h4>{{x[2][0]}}:{{x[2][1]}}-{{x[2][2]}}:{{x[2][3]}}</h4>
                        {% else: %}
                            <h4>{{dagar[x[3]-1]}}  {{x[2][0]}}:{{x[2][1]}}-{{x[2][2]}}:{{x[2][3]}}</h4>
                        {% endif %}

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
                {% endif %}

            {% else: %}
                <div class="ui segment">
                    <h2>Ekkert fannst</h2>
                </div>
            {% endif %}
        </div>
    </div>
    <script>
        $('.ui.sticky')
            .sticky({
            context: '#val'
        });
    </script>
</div>
<footer> 
    <p style="margin-top:4px;">© 2018&nbsp;Kolbeinn Ingólfsson&nbsp;&nbsp;&nbsp;
        <a href="https://github.com/KolbeinnIn/LokaverkefniVEF/wiki" target="_blank">
            <img style="position:relative;top:4px;" src="../static/github.svg" height="16" width="16">
        </a>
    </p>
</footer>