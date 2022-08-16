package donbal;

import java.time.Instant;

public class Message {
  private String line;
  private Instant timestamp;

  public Message() {
  }

  public Message(String line, Instant timestamp) {
    this.line = line;
    this.timestamp = timestamp;
  }

  public String getLine() {
    return line;
  }

  public void setLine(String line) {
    this.line = line;
  }

  public Instant getTimestamp() {
    return timestamp;
  }

  public void setTimestamp(Instant timestamp) {
    this.timestamp = timestamp;
  }
}
