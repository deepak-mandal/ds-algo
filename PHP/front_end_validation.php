<div class="container">
            <center><h4>Front end validation</h4></center>
            <div class="row">
                <div class="col-xs-4 col-xs-offset-4">
                    <div class="panel panel-primary">
                        <div class="panel-heading"><h4>Login</h4></div>
                        <div class="panel-body">
                            <form>
                                <div class="form-group">
                                    <input type="email" class="form-control" placeholder="Email" name="email" required="true" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$">
                                </div>
                                <div class="form-group">
                                    <input type="password" class="form-control" placeholder="password" name="password" required="true" pattern=".{6,}">
                                </div>   
                                <button type="submit" name="submit" class="btn btn-primary">Login</button>
                            </form><br>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        
