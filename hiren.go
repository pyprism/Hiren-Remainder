package main

import (
	//"net/http"

	"github.com/labstack/echo"
	"github.com/pyprism/Hiren-Reminder/controllers"
	"github.com/labstack/echo/middleware"
)

func main() {
	e := echo.New()
	// middleware
	e.Use(middleware.Logger())
	e.Use(middleware.Recover())
	e.Use(middleware.CSRF())
	e.Use(middleware.Gzip())
	e.Use(middleware.RequestID())
	e.Use(middleware.BodyLimit("2M"))
	e.Use(middleware.Secure())

	// static files
	e.Static("/static", "static")
	//e.File("/favicon.ico", "static/favicon.ico")

	e.GET("/", controllers.Index)
	//e.GET("/hello/", controllers.X)
	e.Logger.Fatal(e.Start(":8000"))
}