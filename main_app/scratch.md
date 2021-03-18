{% comment %} <header class="navbar">
        <div class="nav">

            <div class="nav-left">
                <div class="brand-logo"> 
                    <a href= "/">
                    
                    <img src="https://thumbs.dreamstime.com/b/sunset-icon-linear-179583112.jpg">
                    </a>
                </div>
            </div>
            <div class="nav-right"> 
                <ul class="nav-links">
                    <li><a href="/"> About Us </a></li>
                {% if user.is_authenticated %}
                    <li><a href="/profile"> View Profile</a></li>
                    <li><a href="{% url 'logout' %}"> Log Out</a></li>
                {% else %}
                    <li><a href={% url 'signup' %}> Sign Up</a></li>
                    <li><a href={% url 'login' %}> Log In</a></li>
                {% endif %}
                </ul>
            </div>

        </div>
    </header>  {% endcomment %}

    {% comment %} <nav class="navbar sticky-top navbar-light">
    <div class="container-fluid">
        <a class="navbar-brand" href="/">
        <img src="{% static '/images/WF_brand.svg' %}" width="100" height="60" alt="">
        Wayfarer
        </a>
        <ul class="nav">
            <li class="nav-item nav-pills nav-fill">
                <a class="nav-link" href="/"> About Us </a>
            </li>
                {% if user.is_authenticated %}
                <li class="nav-item nav-pills nav-fill">
                    <a class="nav-link" href="/profile"> View Profile</a>
                </li>
                <li class="nav-item nav-pills nav-fill">
                    <a class="nav-link" href="{% url 'logout' %}"> Log Out</a>
                </li>
                {% else %}
                <li class="nav-item nav-pills nav-fill">
                    <a class="nav-link" href={% url 'signup' %}> Sign Up</a>
                </li>
                <li class="nav-item nav-pills nav-fill">
                    <a class="nav-link" href={% url 'login' %}> Log In</a>
                </li>
                {% endif %}

        </ul>
    </div>
    </nav>
    <form action="{% url 'search_results' %}" method="get">
        <input name="q" type="text" placeholder="Search...">
    </form>  {% endcomment %}


{% comment %} <nav class="navbar sticky-top navbar-light">
    <div class="container-fluid">
        <a class="navbar-brand" href="/">
        <img src="*/*/static/images/WF-brand" width="150" height="60" alt="">
        </a>
        <ul class="nav">
            <li class="nav-item nav-pills nav-fill">
                <a class="nav-link" href="/"> About Us </a>
            </li>
                {% if user.is_authenticated %}
                <li class="nav-item nav-pills nav-fill">
                    <a class="nav-link" href="/profile"> View Profile</a>
                </li>
                <li class="nav-item nav-pills nav-fill">
                    <a class="nav-link" href="{% url 'logout' %}"> Log Out</a>
                </li>
                {% else %}
                <li class="nav-item nav-pills nav-fill">
                    link to signup BS modal 
                    <a class="nav-link" data-bs-toggle="modal" data-bs-target="#exampleModal"> Sign Up</a>
                    BS modal box
                    <div class="modal" tabindex="-1">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title">SignUp Form</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="modal-body">
                                        {% if error_message %}
                                            <p class="red-text">{{ error_message }}</p>
                                        {% endif %}

                                        <form method="POST" action="{% url 'signup' %}">
                                            {% csrf_token %}
                                            {{ form.as_p }}
                                            <input type="submit" class="btn" value="signup">
                                        </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>
                <li class="nav-item nav-pills nav-fill">
                    <a class="nav-link" href={% url 'login' %}> Log In</a>
                </li>
                {% endif %}

        </ul>
    </div>
    </nav> {% endcomment %}