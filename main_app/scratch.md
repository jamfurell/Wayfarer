base.html--- body background img
  <style>
        body {
         
            background-repeat: no-repeat;
            {% comment %} background-attachment: fixed; {% endcomment %}
            background-size: 100%;
            overflow: hidden;
        }
    </style>
    
navbar color: rgb(40 11 88)
profile-citylist img placehodler: https://images.cdn2.stockunlimited.net/preview1300/night-view-of-city-with-shooting-stars_1522096.jpg
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
    ___________________________________________________
    >>>>>Accordion for city-detail page > my city list
               <div class="accordion" id="accordionExample">
                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingOne">
                    <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                        My Cities
                    </button>
                    </h2>
                    <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                    <div class="accordion-body">
                        {% for review in my_reviews %}
                            <div class="card text-dark bg-light mb-3" >
                                <div class="card-body">
                                    <h5 class="card-title">{{ review.city }}</h5>
                            {% comment %} <p class="card-text"></p> {% endcomment %}
                                <a href="{% url 'show_review' review.id %}" class="btn btn-sm btn-outline-info">See My Review</a>
                                </div>
                            </div>
                        {% endfor %}
                    </div>
                    </div>
                </div>
            </div>