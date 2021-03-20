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

                            {% comment %} {% for review in my_reviews %}
                <div class="card text-dark bg-light mb-3" >
                    <div class="card-body">
                        <h5 class="card-title">{{ review.city }}</h5>
                        <p class="card-text">{{review.title}}</p>
                    <a href="{% url 'show_review' review.id %}" class="btn btn-sm btn-outline-info">See My Review</a>
                    </div>
                </div>
                {% endfor %} {% endcomment %}
            

        {% comment %} </div> {% endcomment %}
_______________________________________
city detail page grid:::

.grid-container {
    display: grid;
    grid-template-columns: 1fr 1.4fr 1fr 1.4fr 1fr 1.4fr 1fr 0.6fr;
    grid-template-rows:  0.7fr 1fr 1fr 1fr 1.4fr ;
    gap: 0px 0px;
    grid-template-areas:
        
        "my-cities my-cities city city city city city ."
        "my-cities my-cities city city city city city ."
        "my-cities my-cities review review review review review ."
        "my-cities my-cities review review review review review ."
        "my-cities my-cities review review review review review .";
    margin-top: 20px;
}
.my-cities {
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows:0.5fr 1fr;
    gap: 0px;
    grid-template-areas:
        "my-cities-title my-cities-title"
        "my-cities-list my-cities-list";
    grid-area: my-cities;
    border-radius: 10px;
}
.accordion-button.collapsed{
    border: 1px solid blue;
}
.my-cities-title { 
    grid-area: my-cities-title;
    background: #d7dcf6; 
}
.my-cities-list { 
    grid-area: my-cities-list;
    /* height: 5rem; */
}
.city {
    display: grid;
    grid-template-columns: 1.2fr 1fr 1fr 0.3fr;
    grid-template-rows: 0.4fr 1.6fr;
    gap: 0px 0px;
    grid-template-areas:
        "city-name city-pic city-pic city-pic"
        ". city-pic city-pic city-pic";
    grid-area: city;
    padding-left: 20px;
}
.city-name { 
    grid-area: city-name; 
}
.city-pic { 
    grid-area: city-pic;
    overflow: hidden;
    /* position: relative; */
}

/* .maintxt > img, .overlay-text {
    position: absolute;} */
/* .city-pic img{
    height: 180px;
    object-fit: cover;
} */
.review {
    display: grid;
    grid-template-columns: 1fr 1.1fr 0.9fr;
    grid-template-rows: 0.4fr 1.6fr 1fr 1fr;
    gap: 0px 0px;
    grid-template-areas:
        "review-title review-title review-btn"
        "review-list review-list review-list"
        "review-list review-list review-list"
        "review-list review-list review-list";
    grid-area: review;
    padding: 10px 20px;
}
.review-title { grid-area: review-title; }
.review-btn { 
    grid-area: review-btn;
    justify-self: end; 
}
.review-list { grid-area: review-list; }
.review-list card{
    height: 6rem;
}
_______________________________________________________________


<div class="grid-container">
    <div class="my-cities text-center">
        {% comment %} <div class="my-cities-title ">
            <h4>My list of Cities</h4>
        </div> {% endcomment %}
        {% comment %} <div class="my-cities-list "> {% endcomment %}
            {% comment %} <ul>
                <li>list city #1</li>
                <li>list city #2</li>
            </ul> {% endcomment %}
            <div class="accordion" id="accordionExample">
                <div class="accordion-item shadow">
                    <h2 class="accordion-header my-cities-title" id="headingOne">
                    <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                        My Cities
                    </button>
                    </h2>
                    <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                    <div class="accordion-body my-cities-list">
                        {% for review in my_reviews %}
                            <div class="card text-dark bg-light mb-3" >
                                <div class="card-body">
                                    <h5 class="card-title">{{ review.city }}</h5>
                                    <p class="card-text">{{review.title}}</p>
                            {% comment %} <p class="card-text"></p> {% endcomment %}
                                <a href="{% url 'show_review' review.id %}" class="btn btn-sm btn-outline-info">See My Review</a>
                                </div>
                            </div>
                        {% endfor %}
                    </div>
                    </div>
                </div>
            </div>

    </div>
    <div class="city text-center">
        <div class="city-name">
            <h4>{{city.name}}</h4>
            <h5> {{city.country}}</h5>
        </div>
        <div class="city-pic">
            {% if city.city_pic %}
                <img class="img-fluid rounded float-end" src="{{ city.city_pic }}" class="rounded" alt="{{city.name}}">
                <span class="overlay-text">Credits to: {{city.photographer}}</span>
            {% else %}
                <img width="600" src="" onerror="this.src='{% static '/images/default_city.jpg' %}';">
            {% endif %}
        </div>
    </div>

    <div class="review">
        <div class="review-title">
            <h5> Reviews for {{city.name}}
        </div>
        <div class="review-btn">

                <!-- Button trigger modal for ADD review -->
                <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@mdo">Add Review</button>
    
                <!-- Modal for ADD form and post-->
                <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="exampleModalLabel">Add New Review</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                            <form method="POST" action="{% url 'add_review' city.id%}">
                                {% csrf_token %}
                                    {% comment %} {{ form.as_p }} {% endcomment %}
                                <div class="mb-3">
                                    <label class="col-form-label" for="id_title">Title:</label>
                                    <input class="form-control" type="text" name="title" maxlength="200" required id="id_title">
                                </div>
                                <div class="mb-3">
                                    <label class="col-form-label" for="id_description">Description:</label>
                                    <input class="form-control" type="text" name="description" maxlength="1000" required id="id_description">
                                </div>
                            </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    <button type="submit" class="btn btn-primary">Add Review</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>



        </div>
        <div class="review-list">


            {% for cityreview in city_reviews %}
            <div class="card mb-3 hadow-sm rounded">
                <div class="row g-0">
                    <div class="col-md-4">
                        <img class="img-thumbnail" src="{{profile.profile_pic}}" alt="...">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <a href="{% url 'show_review' cityreview.id %}" ><h5 class="card-title">{{cityreview.title}}</h5></a>
                            <p class="card-text">{{cityreview.description}}</p>
                            <p class="card-text"><small class="text-muted">Created: {{cityreview.created_at}}</small></p>
                        </div>

                        <!-- Button trigger modal for DELETE review -->
                        <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#exampleModal2">
                        Delete Review
                        </button>

                        <!-- Modal for DELETE alert message and post-->
                        <div class="modal fade" id="exampleModal2" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="exampleModalLabel">Delete Review</h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                    <form method="POST" action="{% url 'delete_review' cityreview.id %}">
                                        {% csrf_token %}
                                        <p> Are you sure you want to delete review for {{city.name}}?<p>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        
                                    
                                        <button type="submit" class="btn btn-danger">Yes, DELETE</button>
                                    </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}



        </div>
        
    </div>
</div>