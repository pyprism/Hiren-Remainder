package main

import (
	"net/http"

	"github.com/labstack/echo"
	"github.com/pyprism/Hiren-Reminder/controllers"
)

func main() {
	e := echo.New()
	e.GET("/", func(c echo.Context) error {
		return c.String(http.StatusOK, "Hello, World! d")
	})
	e.GET("/hello/", controllers.X)
	e.Logger.Fatal(e.Start(":8000"))
}