# Calendar Proxy

This project provides a REST API for fetching, managing, and exporting calendar events. Acting as a proxy, it retrieves calendar data from an external iCalendar source, supports user-added events, and offers a flexible interface for event management. Additionally, it generates a subscription link compatible with calendar applications, enabling seamless integration and real-time updates.

---

## Features

- **Fetch Events**: Sync calendar events from a remote iCalendar source and store them in JSON format.
- **Add Custom Events**: Create custom user-defined events.
- **Update Events**: Modify existing events based on specific criteria.
- **Delete Events**: Remove specific events from the calendar.
- **Export as iCalendar**: Generate and export an updated `.ics` file, which can
  be subscribed.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/calendar-proxy.git
   cd calendar-proxy
   ```


2.	Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up configuration:
   - Update the `CALENDAR_URL` variable in the script to point to your iCalendar source.
   - Ensure the `JSON_FILE` and `DELETED_EVENTS_FILE` paths are set correctly.

4. Run the application.

    ```bash
    python src/calendar_proxy.py
    ```



## Usage

The application runs on `http://127.0.0.1:5000`. Below are the API endpoints:

### Fetch and Manage Events

#### Fetch Events
- **URL**: `/events`
- **Method**: `GET`
- **Description**: Retrieves all stored events in JSON format.

#### Add Event
- **URL**: `/create`
- **Method**: `GET`
- **Parameters**:
  - `title`: Event title.
  - `start`: Start date/time (ISO format).
  - `end`: End date/time (ISO format).
  - `location`: Event location.
- **Example**: Create a meeting with a title, start time, end time, and location.

```url
/create?title=Meeting&start=2025-02-04T15:00:00Z&end=2025-02-04T16:00:00Z&location=Office
```


#### Update Event
- **URL**: `/update`
- **Method**: `GET`
- **Parameters**:
  - `current_title`: Current event title.
  - `current_start`: Current start date/time (optional).
  - `current_end`: Current end date/time (optional).
  - `new_title`: New title (optional).
  - `new_start`: New start date/time (optional).
  - `new_end`: New end date/time (optional).
- **Example**: Update a meeting's title or time range.

```
/update?current_title=Meeting&new_title=Team Meeting
```



#### Delete Event
- **URL**: `/delete`
- **Method**: `GET`
- **Parameters**:
  - `current_title`: Title to identify the event (optional).
  - `current_start`: Start date/time (optional).
  - `current_end`: End date/time (optional).
- **Example**: Delete a specific event by title or time.

```
/delete?current_title=Meeting
```

---


### Export Events

#### Export as iCalendar
- **URL**: `/export_ical`
- **Method**: `GET`
- **Description**: Generates an `.ics` file with all current events and provides
  it for download. <p style="color:#007BFF;">**Can be subscribed with your calendar application!**</p>

---

## Data Storage

- **`events.json`**: Stores all event data locally.
- **`deleted_events.json`**: Tracks events deleted from the remote calendar to
  prevent re-importing from the source calendar.

---

## Development

### Prerequisites

- **Python 3.8 or higher**
- Required Python libraries:
  - `Flask`
  - `icalendar`
  - `requests`

### Adding a New Feature

1. Implement the logic in the respective function in `app.py`.
2. Update the API documentation in this README if necessary.
3. Test your changes locally before deployment.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

**Frederik Schinner** | [f@schinner.dev](mailto:f@schinner.dev)