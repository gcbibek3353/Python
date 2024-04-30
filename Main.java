class LL {
    private class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    private Node head;

    public void addFirst(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        newNode.next = head;
        head = newNode;
    }

    public void addLast(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node currentNode = head;
        while (currentNode.next != null) {
            currentNode = currentNode.next;
        }
        currentNode.next = newNode;
    }

    public void delFirst() {
        if (head == null) {
            System.out.println("the list is empty");
            return;
        }
        head = head.next;
    }

    public void delLast() {
        if (head == null) {
            System.out.println("the list is empty");
            return;
        } else if (head.next == null) {
            head = null;
        } else {
            Node secondLastNode = head;
            Node lastNode = head.next;
            while (lastNode.next != null) {
                secondLastNode = secondLastNode.next;
                lastNode = lastNode.next;
            }
            secondLastNode.next = null;
        }
    }

    public void reverseList() {
        if (head == null || head.next == null) {
            return;
        }

        Node prevNode = null;
        Node currNode = head;
        while (currNode != null) {
            Node nextNode = currNode.next;
            currNode.next = prevNode;
            prevNode = currNode;
            currNode = nextNode;
        }
        head = prevNode;
    }

    public void printList() {
        if (head == null) {
            System.out.println("the list is empty");
            return;
        }
        Node currentNode = head;
        while (currentNode != null) {
            System.out.print(currentNode.data + " -> ");
            currentNode = currentNode.next;
        }
        System.out.println("null");
    }
}

public class Main {
    public static void main(String[] args) {
        LL list = new LL();

        list.addFirst(1);
        list.addFirst(2);
        list.addLast(3);
        list.addLast(4);
        list.printList();
        list.reverseList();
        list.printList();
    }
}
