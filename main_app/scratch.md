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
------------------------------------------------------------------------------------------------
CAN USE FOR ABOUT US PAGE- LINKS TO GH/LI....
                    <div class="card mt-3">
                        <ul class="list-group list-group-flush">
                        <li class="list-group-item d-flex justify-content-between align-items-center flex-wrap">
                            <h6 class="mb-0"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-globe mr-2 icon-inline"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>Website</h6>
                            <span class="text-secondary">https://bootdey.com</span>
                        </li>
                        <li class="list-group-item d-flex justify-content-between align-items-center flex-wrap">
                            <h6 class="mb-0"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-github mr-2 icon-inline"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>Github</h6>
                            <span class="text-secondary">bootdey</span>
                        </li>
                        <li class="list-group-item d-flex justify-content-between align-items-center flex-wrap">
                            <h6 class="mb-0"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-twitter mr-2 icon-inline text-info"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg>Twitter</h6>
                            <span class="text-secondary">@bootdey</span>
                        </li>
                        <li class="list-group-item d-flex justify-content-between align-items-center flex-wrap">
                            <h6 class="mb-0"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-instagram mr-2 icon-inline text-danger"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>Instagram</h6>
                            <span class="text-secondary">bootdey</span>
                        </li>
                        <li class="list-group-item d-flex justify-content-between align-items-center flex-wrap">
                            <h6 class="mb-0"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-facebook mr-2 icon-inline text-primary"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>Facebook</h6>
                            <span class="text-secondary">bootdey</span>
                        </li>
                        </ul>
                    </div>
==========================================================================
/Profile page- with temp profile card 

.profile-card {
    height: 200px;
    border: none;
    border-radius: 10px;
    background-color: rgb(250, 248, 219)
}

.stats {
    background: #f2f5f8 !important;
    color: #000 !important
}

.articles {
    font-size: 10px;
    color: #a1aab9
}

.number1 {
    font-weight: 500
}

<div class="profile-grid-container">
    <div class="container mt-5 d-flex">
        {% comment %} <div class=""> {% endcomment %}
            <div class="profile-card p-3 text-center">
                <div class="d-flex align-items-center">
                    <div class="image"> <img src="https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=80" class="rounded" width="155"> </div>
                    <div class="ml-3 w-100">
                        <h4 class="mb-0 mt-0">{{profile.user.username}}</h4> 
                        {% comment %} <span>Senior Journalist</span> {% endcomment %}
                        <div class="p-2 mt-2 bg-primary d-flex justify-content-between rounded text-white stats">
                            <div class="d-flex flex-column">
                                <span class="articles">Join Date</span>
                                <span class="number1">{{profile.user.date_joined}}</span> 
                            </div>
                        </div>
                        <div class="button mt-2 d-flex flex-row align-items-center"> 
                            {% if user.username == profile_user %}
                                <a href="{% url 'edit_profile' %}">Edit Profile</a>
                            {% endif %}
                        </div>
                    </div>
                </div>
            </div>
        {% comment %} </div> {% endcomment %}
    </div>

        {% comment %} <img src="" class="profile_picture" onerror="this.src='{% static '/images/default_city.jpg' %}';">
    </div>

    <div class="profile-name">
        <h1>{{ profile.user.username }}</h1>
        {% if user.username == profile_user %}
            <a href="{% url 'edit_profile' %}">Edit Profile</a>
        {% endif %}
    </div>

    <div class="profile-info">
        <p> Current City: {{ profile.current_city }}</p>
        <p>Member Since {{profile.user.date_joined}}</p>
    </div> {% endcomment %}

    <div class="profile-reviews">
        <div class="row text-center">
            {% for review in reviews %}
            <div class="col-sm-6">
                <div class="card" style="width: 18rem;">
                    <img src="{{ review.city.city_pic }}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{{ review.title }}</h5>
                        {% comment %} <p class="card-text"></p> {% endcomment %}
                        <a href="{% url 'show_review' review.id %}" class="btn btn-outline-primary">See My Review</a>
                    </div>
                </div>

            {% comment %} <p>{{ review.description }} </p> {% endcomment %}
            {% endfor %}
        
            </div>
        </div>
    </div>
</div>


-----------------------------------------------------------------------------
CSS for carousel template and navbar

/* 
.nav{
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 35px;
    background-color: rgb(96, 173, 245);
}
.nav-left{
    width: 20%; 
    height: 100%;
    overflow: hidden;
}
.brand-logo{
    width: 100%;
    height: 100%;

}
.brand-logo img{

    object-fit: cover;
}
.nav-right{
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center; 
    width: 80%;
    height: 100%;
} 
.nav-links li{
    color:white;
    display: inline-block;
    padding-right: 5px;
}
.container{
    margin: 1rem auto;
    width: 90%;
}
.homepage{
    text-align: center;
}
.homepage-images{
    overflow: hidden;
}
.homepage-images img {
    height: 160px;
    object-fit: cover;
}

/* SLIDSHOW */
.mySlides {
	display: none;
	height: 100%;
	font-family: Arial,Helvetica,sans-serif;
}
.mySlides img {
	width: 100%;
	height: 100%;
}
.slideshow-container {
	overflow: hidden;
	position: relative;
	margin: auto;
	width: 500px;
	height: 200px;
}
.slide-prev, .slide-next {
	cursor: pointer;
	position: absolute;
	top: 50%;
	width: auto;
	padding: 16px;
	margin-top: -22px;
	color: white;
	font-weight: bold;
	font-size: 18px;
	transition: 0.6s ease;
	border-radius: 0 3px 3px 0;
}
.slide-next {
	right: 0;
	border-radius: 3px 0 0 3px;
}
.slide-prev:hover, .slide-next:hover {
	background-color: rgba(0,0,0,0.8);
}
.slide-text {
	color: #f2f2f2;
	font-size: 15px;
	padding: 8px 12px;
	position: absolute;
	bottom: 8px;
	width: 100%;
	text-align: center;
	text-shadow: 0px 0px 2px #000;
}
.slide-dot-control {
	text-align: center;
	margin-top: 10px;
}
.slide-dot {
	cursor:pointer;
	height: 13px;
	width: 13px;
	margin: 0 2px;
	background-color: #bbb;
	border-radius: 50%;
	display: inline-block;
	transition: background-color 0.6s ease;
}
.slide-dot-active, .slide-dot:hover {
	background-color: #717171;
}

/************CSS Animation***********/

.animated { 
    -webkit-animation-name: fadeInLeft; 
            animation-name: fadeInLeft; 
    -webkit-animation-duration: 1s; 
            animation-duration: 1s; 
} 
@-webkit-keyframes fadeInLeft { 
    0% { 
        opacity: 0; 
        -webkit-transform: translateX(-20px); 
    } 
    100% { 
        opacity: 1; 
        -webkit-transform: translateX(0); 
    } 
} 
@keyframes fadeInLeft { 
    0% { 
        opacity: 0; 
        transform: translateX(-20px); 
    } 
    100% { 
        opacity: 1; 
        transform: translateX(0); 
    } 
} 
.fadeInLeft { 
    -webkit-animation-name: fadeInLeft; 
    animation-name: fadeInLeft; 
} 

__________________________________________________________________________
base.html removed code

    <style>
        body {

            background-repeat: no-repeat;
            {% comment %} background-attachment: fixed; {% endcomment %}
            background-size: 100%;
            object-fit: contain;
        }
    </style>
